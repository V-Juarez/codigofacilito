class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
