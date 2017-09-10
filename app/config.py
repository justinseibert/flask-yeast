import os
from .site import site
from .api import api
from .admin import admin

class DefaultConfig(object):
    # default config inherited by all

    PROJECT = 'project'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    DEBUG = False
    ASSETS_DEBUG = False

    ADMINS = ['name@email.com']

    SECRET_KEY = 'secret key'

    EXTENSIONS = [
        {
            'name': 'js_all',
            'bundle': [
                'site/js/script1.js',
                'site/js/script2.js'
            ],
            'filters': 'jsmin',
            'output': 'site/js/all.min.js'
        },
        {
            'name': 'sass_all',
            'bundle': [
                'site/sass/style1.scss',
                'site/sass/style2.sass'
            ],
            'filters': 'libsass,cssmin',
            'output': 'site/css/all.min.css'
        }
    ]
    BLUEPRINTS = [site, api]

class DevConfig(DefaultConfig):
    # config for the development environment

    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    ASSETS_DEBUG = True

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
