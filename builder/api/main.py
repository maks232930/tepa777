from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm.exc import UnmappedInstanceError

from builder.models.result import Result, results_schema, result_schema
from builder.extensions import db
from builder.utils import check_result


class MainApi(Resource):
    def get(self):
        result = Result.query.all()
        return results_schema.dump(result)

    def post(self):
        json_input = request.get_json()
        try:
            form = result_schema.load(json_input)
            if len(form.get('data')) == 0:
                raise ValidationError('Empty data')

            result = check_result(form.get('data'))

            if not result:
                raise ValidationError('Empty data')

        except ValidationError as err:
            return {"errors": err.messages}, 422

        db.session.add(result)
        db.session.commit()
        return result_schema.dump(result)
