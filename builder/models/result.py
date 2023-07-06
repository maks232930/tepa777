from sqlalchemy import Column, JSON
from builder.extensions import ma
from .base import Base


class Result(Base):
    __tablename__ = 'result'

    data = Column(JSON, nullable=False)


class ResultSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Result


result_schema = ResultSchema()
results_schema = ResultSchema(many=True)
