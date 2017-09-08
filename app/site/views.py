from flask import render_template
from . import site

@site.route('/', methods=['GET'])
def index():
    return 'this is the main site homepage'
