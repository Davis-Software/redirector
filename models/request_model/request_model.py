from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.ext.mutable import MutableDict, MutableList
from sqlalchemy.orm import relationship


class RedirectModel(BaseModel):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True)

    redirect_id = Column(Integer, ForeignKey("redirects.id"))
    redirect = relationship("RedirectModel", back_populates="requests")

    from_ip = Column(String(255))
    from_trace = Column(MutableList.as_mutable(JSON))
    from_user_agent = Column(String(4096))
    referrer = Column(String(4096))
    parameters = Column(MutableDict.as_mutable(JSON))
