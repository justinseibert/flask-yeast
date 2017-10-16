import sqlite3
from flask import render_template, abort

from EXAMPLE_APP import database as Database
from EXAMPLE_APP.views import _admin

@_admin.route('/')
def index():
    return render_template('admin/index.html')
