import datetime
import json

from flask import jsonify
from sqlalchemy import Column, String, Text
from sqlalchemy.orm.collections import InstrumentedList

from __init__ import db


class BaseModel(db.Model):
    __abstract__ = True

    def add(self, commit=True):
        db.session.add(self)

        if commit:
            self.commit()

    def delete(self, commit=True):
        db.session.delete(self)

        if commit:
            self.commit()

    def commit(self):
        db.session.commit()

    def to_dict(self, show: list = None, to_json=True, parent_type = None):
        columns = self.__table__.columns.keys()
        relationships = self.__mapper__.relationships.keys()

        def is_jsonable(x):
            try:
                json.dumps(x)
                return True
            except (TypeError, OverflowError):
                return False

        ret_data = {}

        for key in columns:
            if key.startswith("_") or key.startswith("__"):
                continue
            if (not show) or key in show:
                if type(getattr(self, key)) == datetime.datetime:
                    ret_data[key] = getattr(self, key).timestamp() * 1000
                    continue
                if to_json and (not is_jsonable(getattr(self, key))):
                    continue
                ret_data[key] = getattr(self, key)

        for key in relationships:
            if key.startswith("_") or key.startswith("__"):
                continue
            if (not show) or key in show:
                if type(getattr(self, key)) is InstrumentedList:
                    ret_data[key] = list(map(
                        lambda x: x.to_dict(show=show, to_json=to_json, parent_type=type(self)),
                        getattr(self, key)
                    ))
                elif parent_type is not None and type(getattr(self, key)) is not parent_type:
                    ret_data[key] = getattr(self, key).to_dict(show=show, to_json=to_json)

        return ret_data

    def to_json(self, show: list = None):
        return jsonify(self.to_dict(show=show))


class KeyedValueModel(BaseModel):
    __abstract__ = True

    key = Column(String(128), nullable=False, primary_key=True)
    value = Column(Text, nullable=False)

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.key}={self.value}>"

    def __str__(self):
        return f"{self.key}={self.value}"

    def to_json(self, show: list = None, to_json=False):
        ret_data = super().to_json(show=show, to_json=to_json)
        ret_data["key"] = self.key
        ret_data["value"] = self.value
        return ret_data

    @classmethod
    def export(cls):
        return cls.query.all()

    @classmethod
    def export_to_dict(cls):
        ret = {}
        for item in cls.export():
            ret[item.key] = item.value
        return ret

    @classmethod
    def set(cls, key: str, value: str):
        item = cls.query.filter_by(key=key).first()
        if item is None:
            item = cls(key, value)
            db.session.add(item)
        else:
            item.value = value
        db.session.commit()
        return item

    @classmethod
    def get(cls, key: str, boolean=False):
        item = cls.query.filter_by(key=key).first()
        if item is None:
            return None
        return item.value if not boolean else item.value in ["True", "true", "1"]

    @classmethod
    def delete_key(cls, key, commit=True):
        item = cls.query.filter_by(key=key).first()
        if item is None:
            return None
        db.session.delete(item)
        if commit:
            db.session.commit()
        return item

    @classmethod
    def get_by_key(cls, key: str):
        return cls.query.filter_by(key=key).first()

    @classmethod
    def get_by_value(cls, value: str):
        return cls.query.filter_by(value=value).first()

    @classmethod
    def get_by_key_value(cls, key: str, value: str):
        return cls.query.filter_by(key=key, value=value).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_all_by_key(cls, key: str):
        return cls.query.filter_by(key=key).all()

    @classmethod
    def get_all_by_value(cls, value: str):
        return cls.query.filter_by(value=value).all()

    @classmethod
    def get_all_by_key_value(cls, key: str, value: str):
        return cls.query.filter_by(key=key, value=value).all()
