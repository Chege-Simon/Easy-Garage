#flask config classes
import os
#  Set Flask configuration vars
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # General Config
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

class DevConfig:
    TESTING = True
    DEBUG = os.environ.get('DEBUG')
    QLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'devdatabase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig:
    TESTING = False
    DEBUG = os.environ.get('DEBUG')
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')