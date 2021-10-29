import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Conf:
  SECRET_KEY = os.environ.get('conf_key')

  SQLALCHEMY_DATABASE_URI = os.environ.get('dbs_url')
  if os.environ.get('dbs_url').startswith('postgres'):
      SQLALCHEMY_DATABASE_URI = os.environ.get('dbs_url').replace('postgres', 'postgresql')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  FLASK_APP = os.environ.get('flsk_app')
  FLASK_ENV = os.environ.get('flsk_env')