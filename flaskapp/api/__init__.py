from flask import Blueprint

bp_api = Blueprint('api', __name__)

from flaskapp.api import offices, persons, helpers
