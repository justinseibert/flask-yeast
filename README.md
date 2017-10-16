# flask-yeast
a Flask starter app with configuration, blueprints, and web-assets extensions

## setup
1. change name of container directory to desired app name
2. change all references of `EXAMPLE_APP` to match desired app directory name
3. remove `-sample` from filenames in top-level directory and configure desired DEVELOPMENT and PRODUCTION variables in config.py

## run in local environment
1. create a virtual environment in app's top-level directory (venv* folder schemes are ignored by .gitignore)
```
$ virtualenv venv3.5 -p python3.5
```
2. install requirements
```
$ . venv3.5/bin/activate
(venv3.5)$ pip install -r requirements.txt
```
3. run the app (\__init__.py should be set to run DEVELOPMENT mode)
```
(venv)$ export FLASK_APP=__init__.py
(venv)$ export FLASK_DEBUG=1
(venv)$ flask run --host=0.0.0.0
```
