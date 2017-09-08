# flask-yeast
a Flask starter app with configuration, blueprints, and web-assets extensions

## run
create a virtual environment outside of the app directory

```
$ virtualenv venv
$ . venv/bin/activate
(venv)$ python run.py 'DEVELOPMENT'
```

## features
- `run.py` creates the app and starts the flask server with configuration environment (DEVELOPMENT or PRODUCTION) set by the system argument, defaults to PRODUCTION
- `app/app.py` creates the app with various configuration, blueprints, extensions, default error pages, etc
- `app/config.py` contains configuration environments and variables
- `app/site/` default location of main site files
  - `views.py` default location for defining routes
- `app/admin` default location for admin files, not included in production environment by default
  - `views.py` default location for defining routes
- `app/api/controls.py` default location for defining api response routes
