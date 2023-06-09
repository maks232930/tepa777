from sqlalchemy import Column, Integer
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from ..extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)


Base = declarative_base(cls=BaseModel)
