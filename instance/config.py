import os

class Config(object):
    ''' Parent Configuration class. '''
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET', 'JJEK8L4G3BCfY0evXDRxUke2zqAzq6i7wL') #default if not found
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevConfig(Config):
    ''' Development Environment Configrations.'''
    DEBUG = True

class TestConfig(Config):
    '''Configurations for Testing using a separate test database.'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL','postgresql://localhost/bucketlist_test')
    DEBUG = True

class StagingConfig(Config):
    '''Configurations for Staging Environment.'''
    DEBUG = True

class ProductionConfig(Config):
    '''Configurations for Production.'''
    DEBUG = False
    Testing = False


app_config = {
    'development': DevConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}