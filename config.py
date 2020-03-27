#flask config classes
import os
#  Set Flask configuration vars

class Config:
    # General Config
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

class DevConfig:
    TESTING = True
    DEBUG = os.environ.get('DEBUG')
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

class ProdConfig:
    TESTING = False
    DEBUG = os.environ.get('DEBUG')
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')