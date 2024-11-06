from datetime import datetime

from models.base_model import BaseModel

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship


class RedirectionRequestModel(BaseModel):
    __tablename__ = "redirection_requests"

    id = Column(Integer, primary_key=True)
    ip = Column(String(255), nullable=False, unique=True)
    user_agents = Column(Text, nullable=False, default="")
    city = Column(String(255), nullable=True)
    region = Column(String(255), nullable=True)
    country = Column(String(255), nullable=True)
    provider = Column(String(255), nullable=True)
    hostname = Column(String(255), nullable=True)

    last_request_time = Column(DateTime, nullable=False)

    redirection_id = Column(Integer, ForeignKey("redirections.id"))

    def __init__(self, redirection_id, ip):
        self.redirection_id = redirection_id
        self.ip = ip
        self.last_request_time = datetime.utcnow()
