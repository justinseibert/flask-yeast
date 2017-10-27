import os

class DefaultConfig(object):
    # default config inherited by all

    SECRET_KEY = 'EXAMPLE_APP-secretkey'
    DATABASE = os.path.join(PROJECT_ROOT, 'EXAMPLE_APP.db')

class DevConfig(DefaultConfig):
    pass

class ProdConfig(DefaultConfig):
    pass

def get_config(MODE):
    SWITCH = {
        'DEVELOPMENT': DevConfig,
        'PRODUCTION': ProdConfig
    }
    return SWITCH[MODE]
