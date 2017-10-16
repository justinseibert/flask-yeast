import os
from EXAMPLE_APP.views import _site, _admin
from EXAMPLE_APP.api import _api

class DefaultConfig(object):
    # default config inherited by all

    PROJECT = 'EXAMPLE_APP'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    ADMINS = ['admin@EXAMPLE_APP.com']
    VERSION = '0.1.0'

    DEBUG = False
    ASSETS_DEBUG = False

    SECRET_KEY = 'EXAMPLE_APP-secretkey'
    DATABASE = os.path.join(PROJECT_ROOT, 'EXAMPLE_APP.db')

    EXTENSIONS = [
        {
            'name': 'js_lib',
            'bundle': [
                '_site/js/jquery.min.js',
                '_site/js/main.js',
            ],
            'filters': 'jsmin',
            'output': '_site/js/lib.min.js'
        },
        {
            'name': 'sass_all',
            'bundle': [
                '_site/sass/normalize.scss',
                '_site/sass/main.sass',
            ],
            'filters': 'libsass,cssmin',
            'output': '_site/css/all.min.css',
            'depends': '_site/sass/*'
        },
    ]
    BLUEPRINTS = [_site, _api, _admin]

class DevConfig(DefaultConfig):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True
    ASSETS_DEBUG = True

class ProdConfig(DefaultConfig):
    # config for production environment
    DEBUG = False
    ASSETS_DEBUG = False

def get_config(MODE):
    SWITCH = {
        'DEVELOPMENT': DevConfig,
        'PRODUCTION': ProdConfig
    }
    return SWITCH[MODE]
