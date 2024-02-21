class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/ecommerce'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True
