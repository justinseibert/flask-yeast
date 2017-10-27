import sqlite3
from flask import render_template, abort

from EXAMPLE_APP import database as Database
from EXAMPLE_APP.views import _site

@_site.route('/')
def index():
    return render_template('site/index.html')
