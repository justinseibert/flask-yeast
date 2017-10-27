import os

class DefaultConfig(object):
    # default config inherited by all

    SECRET_KEY = 'EXAMPLE_APP-secretkey'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(PROJECT_ROOT, 'EXAMPLE_APP.db')

class DevConfig(DefaultConfig):
    DEV_API_PUBLIC_KEY = 'EXAMPLE_APP-development-api-public-key'
    DEV_API_PRIVATE_KEY = 'EXAMPLE_APP-development-api-PRIVATE-key'
    pass

class ProdConfig(DefaultConfig):
    PROD_API_PUBLIC_KEY = 'EXAMPLE_APP-production-api-public-key'
    PROD_API_PRIVATE_KEY = 'EXAMPLE_APP-production-api-PRIVATE-key'
    pass

def get_config(MODE):
    SWITCH = {
        'DEVELOPMENT': DevConfig,
        'PRODUCTION': ProdConfig
    }
    return SWITCH[MODE]
