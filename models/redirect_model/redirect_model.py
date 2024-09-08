from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class RedirectModel(BaseModel):
    __tablename__ = 'redirects'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False)
    name = Column(String(1024), nullable=False)
    code = Column(String(1024), nullable=False)
    active = Column(Boolean, nullable=False, default=True)

    namespace = Column(String(1024), nullable=False)
    is_file = Column(Boolean, nullable=False, default=False)
    filename = Column(String(1024), nullable=False)

    target_url = Column(String(4096), nullable=True)

    requests = relationship("RequestModel", back_populates="redirects")
