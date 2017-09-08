import os
from .site import site
from .api import api
from .admin import admin

class DefaultConfig(object):
    # default config inherited by all

    PROJECT = 'project'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    DEBUG = False
    TESTING = False
    ASSETS_DEBUG = False

    ADMINS = ['name@email.com']

    SECRET_KEY = 'secret key'

    EXTENSIONS = []
    BLUEPRINTS = [site, api]

class DevConfig(DefaultConfig):
    # config for the development environment

    DEBUG = True
    TESTING = True
    ASSETS_DEBUG = True

    EXTENSIONS = [
        {
            'name': 'js_all',
            'bundle': ('jquery.js', 'base.js'),
            'filters': 'jsmin',
            'output': 'gen/all.min.js'
        }
    ]
    BLUEPRINTS = [site, api, admin]

class ProdConfig(DefaultConfig):
    # config for production environment
    pass

def get_config(MODE):
    SWITCH = {
        'DEVELOPMENT': DevConfig,
        'PRODUCTION': ProdConfig
    }
    return SWITCH[MODE]
