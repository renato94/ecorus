from cerberus import Validator
from models import PersonValidator, OfficeValidator
from api import bp
from flask import request


def bad_request(message='bad request', status_code=400):
    return message, status_code


@bp.before_request
def valid_api_request(update_can_create=False):
    req = request
    if 'api/persons' in req.url:
        object_validator = PersonValidator
    elif 'api/offices' in req.url:
        object_validator = OfficeValidator
    validator = Validator()
    if req.method == 'PUT':
        schema_to_validate = object_validator.create_schema if update_can_create else object_validator.update_schema
        if not validator.validate(req.json, schema_to_validate):
            bad_request(validator.errors)
    if req.method == 'POST' and not validator.validate(req.json, object_validator.create_schema):
        bad_request(validator.errors)
