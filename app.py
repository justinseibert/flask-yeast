import os
from flask import Flask, g, render_template
from flask_assets import Environment, Bundle
from flask_wtf.csrf import CSRFProtect

from EXAMPLE_APP import config_public as ConfigPublic
from EXAMPLE_APP import config_private as ConfigPrivate

def create_app(config='PRODUCTION', app_name=None):
    app_name = ConfigPublic.DefaultConfig.PROJECT
    public = ConfigPublic.get_config(config)
    private = ConfigPrivate.get_config(config)
    blueprints = config.BLUEPRINTS
    extensions = config.EXTENSIONS

    app = Flask(app_name)
    assets = Environment(app)
    csrf = CSRFProtect(app)

    configure_app(app, public, private)
    configure_blueprints(app, blueprints)
    configure_extensions(assets, extensions)

    configure_hook(app)
    configure_logging(app)
    configure_error_handlers(app)

    return app

def configure_app(app, public,private):
    app.config.from_object(private)
    app.config.from_object(public)

def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_extensions(assets, extensions):
    for extension in extensions:
        try:
            depends = extension['depends']
        except:
            depends = ''

        assets.register(extension['name'], Bundle(
            *extension['bundle'],
            filters=extension['filters'],
            output=extension['output'],
            depends=depends
        ))

def configure_hook(app):
    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()

def configure_logging(app):
    pass

def configure_error_handlers(app):
    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('error/500.html', error='500'), 404

    @app.errorhandler(404)
    def notfound_error_page(error):
        return render_template('error/404.html', error='404'), 404
