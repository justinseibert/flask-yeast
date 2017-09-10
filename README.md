# flask-yeast
a Flask starter app with configuration, blueprints, and web-assets extensions

## run
in local environment

```
(venv)$ export FLASK_APP=dev.py
(venv)$ export FLASK_DEBUG=1
(venv)$ flask run --host=0.0.0.0
```

## features
- `dev.py` run the development configuration (does not minify js/css)
- `pro.py` run the production configuration

- `app/app.py` creates the app with various configuration, blueprints, extensions, default error pages, etc
- `app/config.py` contains configuration environments and variables
- `app/site/` default location of main site files
  - `views.py` default location for defining routes
- `app/admin` default location for admin files, not included in production environment by default
  - `views.py` default location for defining routes
- `app/api/controls.py` default location for defining api response routes
