from uuid import uuid4
from datetime import datetime

from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Boolean, BLOB
from sqlalchemy.orm import relationship


class RedirectionModel(BaseModel):
    __tablename__ = "redirections"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    icon = Column(BLOB, nullable=True)
    slug = Column(String(255), nullable=False, unique=True)

    clicks = Column(Integer, default=0)
    enabled = Column(Boolean, default=True)
    archived = Column(Boolean, default=False)

    sub_redirects = relationship("SubRedirectionModel")
    requests = relationship("RedirectionRequestModel")

    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    def __init__(self, name: str, url: str, slug: str = None):
        self.name = name
        self.url = url
        self.slug = slug or self.generate_slug()
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    @staticmethod
    def generate_slug():
        return str(uuid4()).replace("-", "")[:8]
