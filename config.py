import os

class Config():
    SECRET_KEY = os.urandom(24)


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
