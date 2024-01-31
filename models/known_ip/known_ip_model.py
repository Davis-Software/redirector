from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from models.base_model import BaseModel


class KnownIPModel(BaseModel):
    __tablename__ = 'known_ips'

    id = Column(Integer, primary_key=True)
    ip_address = Column(Text, nullable=False)
    access_count = Column(Integer, nullable=False, default=1)
    time_stamp = Column(DateTime, nullable=False)

    redirect_id = Column(Integer, ForeignKey("redirects.id"))
    redirect = relationship("RedirectModel", back_populates="known_ips")

    def __init__(self, redirect_id: int, ip_address: str):
        self.redirect_id = redirect_id
        self.ip_address = ip_address
        self.time_stamp = datetime.utcnow()
