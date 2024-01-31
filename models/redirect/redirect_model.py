from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from models.base_model import BaseModel
from models.request.request_model import RequestModel
from models.known_ip.known_ip_model import KnownIPModel


class RedirectModel(BaseModel):
    __tablename__ = 'redirects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False, unique=True)
    url = Column(String(1000), nullable=False)
    active = Column(Boolean, nullable=False, default=True)

    last_ip = Column(String(255), nullable=True)
    last_referrer = Column(String(4096), nullable=True)
    last_user_agent = Column(String(4096), nullable=True)

    requests = relationship("RequestModel", back_populates="redirect")
    known_ips = relationship("KnownIPModel", back_populates="redirect")

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    last_loaded_at = Column(DateTime, nullable=True)

    def __init__(self, name: str, slug: str, url: str):
        self.name = name
        self.slug = slug
        self.url = url
        self.active = True

        self.last_ip = None
        self.last_user_agent = None
        self.last_referrer = None

        self.requests = []
        self.known_ips = []

        self.last_downloaded_at = None

    def update(self):
        self.updated_at = datetime.utcnow()
        self.commit()

    def edit(self, name: str = None, slug: str = None, url: str = None, active: bool = None):
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if url is not None:
            self.url = url
        if active is not None:
            self.active = active
        self.update()

    def download_request(self, ip: str, user_agent: str, referrer: str, args: str):
        self.last_ip = ip
        self.last_user_agent = user_agent
        self.last_referrer = referrer
        self.last_loaded_at = datetime.utcnow()

        self.requests.append(
            RequestModel(self.id, ip, user_agent, referrer, args)
        )
        ip_model = KnownIPModel.query.filter_by(redirect_id=self.id, ip_address=ip).first()
        if ip_model is None:
            ip_model = KnownIPModel(self.id, ip)
            self.known_ips.append(ip_model)
        else:
            ip_model.access_count += 1

        self.update()

    @property
    def load_count(self):
        return len(self.requests)

    def get_ip_count(self, ip: str):
        ip_model = KnownIPModel.query.filter_by(redirect_id=self.id, ip_address=ip).first()
        if ip_model is None:
            return 0
        return ip_model.access_count

    def delete(self):
        for request in self.requests:
            request.delete()
        for ip in self.known_ips:
            ip.delete()
        super().delete()
