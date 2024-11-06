from models.base_model import BaseModel

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class SubRedirectionModel(BaseModel):
    __tablename__ = "sub_redirections"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    parameter = Column(String(255), nullable=False)

    redirection_id = Column(Integer, ForeignKey("redirections.id"))

    def __init__(self, redirection_id: int, name: str, parameter: str):
        self.redirection_id = redirection_id
        self.name = name
        self.parameter = parameter
