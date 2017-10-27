from flask import Blueprint
_api = Blueprint('api', __name__, url_prefix='/api')

from EXAMPLE_APP.api import _api
