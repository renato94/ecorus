from cerberus import Validator
from flaskapp.models import PersonValidator, OfficeValidator
from flaskapp.api import bp_api
from flask import request, jsonify


def bad_request(errors):
    response = jsonify(errors=errors)
    response.status_code = 400
    return response


@bp_api.before_request
def valid_api_request():
    req = request
    if 'api/persons' in req.url:
        object_validator = PersonValidator
    elif 'api/offices' in req.url:
        object_validator = OfficeValidator
    validator = Validator()
    if req.method == 'PUT' and validator.validate(req.json, object_validator.update_schema) is False:
        return bad_request(validator.errors)
    if req.method == 'POST' and validator.validate(req.json, object_validator.create_schema) is False:
        return bad_request(validator.errors)


@bp_api.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"success": "ok"})
