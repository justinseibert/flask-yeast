#!/bin/bash

. venv3.5/bin/activate
export FLASK_APP=__init__.py
export FLASK_DEBUG=1
export PYTHONDONTWRITEBYTECODE=1
flask run --host=0.0.0.0
