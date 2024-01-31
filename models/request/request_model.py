from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from models.base_model import BaseModel


class RequestModel(BaseModel):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    ip_address = Column(Text, nullable=False)
    user_agent = Column(Text, nullable=False)
    referrer_url = Column(Text, nullable=False)
    request_args = Column(Text, nullable=False)
    time_stamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    redirect_id = Column(Integer, ForeignKey("redirects.id"))
    redirect = relationship("RedirectModel", back_populates="requests")

    def __init__(self, redirect_id: int, ip_address: str, user_agent: str, referrer_url: str, request_args: str):
        self.redirect_id = redirect_id
        self.ip_address = ip_address
        self.user_agent = user_agent
        self.referrer_url = referrer_url
        self.request_args = request_args
        self.time_stamp = datetime.utcnow()
