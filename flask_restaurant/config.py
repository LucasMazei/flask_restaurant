import os.path
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#print('sqlite:///' + os.path.join(basedir, 'storage.db'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "senha"
