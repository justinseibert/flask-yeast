from flask import make_response, jsonify
from . import api

@api.route('/', methods=['GET'])
def index():
    data = {'data' : 'this is a json response'}
    return make_response(jsonify(data))
