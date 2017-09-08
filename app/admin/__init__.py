from flask import Blueprint
admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static', url_prefix='/admin')

from . import views
