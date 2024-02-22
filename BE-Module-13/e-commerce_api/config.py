class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/ecommerce'
    SECRET_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTcwODYxMjI2MCwiaWF0IjoxNzA4NjEyMjYwfQ.cdDAftOQ5kp9PEOLSuVlrmqhkD4zFF5lbvBX3ysNJI8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True
