from sqlalchemy import Column, JSON
# from sqlalchemy.dialects.postgresql import JSON
from .base import Base


class Result(Base):
    __tablename__ = 'result'

    data = Column(JSON, nullable=False)
