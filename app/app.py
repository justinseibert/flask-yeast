import os
from flask import Flask
from flask_assets import Environment, Bundle

import app.config as Config

def create_app(config='PRODUCTION', app_name=None):
    app_name = Config.DefaultConfig.PROJECT
    configurations = Config.get_config(config)
    blueprints = configurations.BLUEPRINTS
    extensions = configurations.EXTENSIONS

    app = Flask(app_name)
    assets = Environment(app)

    configure_app(app, configurations)
    configure_blueprints(app, blueprints)
    configure_extensions(assets, extensions)

    configure_hook(app)
    configure_logging(app)
    configure_error_handlers(app)

    return app

def configure_app(app, configurations):
    app.config.from_object(configurations)

def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_extensions(assets, extensions):
    for extension in extensions:
        assets.register(extension['name'], Bundle(
            *extension['bundle'],
            filters=extension['filters'],
            output=extension['output']
        ))

def configure_hook(app):
    @app.before_request
    def before_request():
        pass

def configure_logging(app):
    pass

def configure_error_handlers(app):
    @app.errorhandler(500)
    def server_error_page(error):
        return "ERROR: SOMETHING WENT WRONG WITH THE SERVER"

    @app.errorhandler(404)
    def notfound_error_page(error):
        return "ERROR: PAGE NOT FOUND"
