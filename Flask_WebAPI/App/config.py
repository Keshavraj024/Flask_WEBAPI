from os import environ, path
from dotenv import load_dotenv

# Current Working Directory
basedir = path.abspath(path.dirname(__file__))
# Pathe of the Environment File
load_dotenv(path.join(basedir, '.env'))

#Base Configuration class
class Config:
	SECRET_KEY = environ.get('SECRET_KEY')
	FLASK_RUN_HOST =environ.get('FLASK_RUN_HOST')
	FLASK_RUN_PORT=environ.get('FLASK_RUN_PORT')
	DEBUG = environ.get('DEBUG')

# Production Configuration
class ProdConfig(Config):
	FLASK_ENV = 'production'
	WTF_CSRF_ENABLED = True

# Development Configuration
class ProdConfig(Config):
	FLASK_ENV = 'development'
	WTF_CSRF_ENABLED = True

# Test Configuration
class TestConfig(Config):
	TESTING = True
	WTF_CSRF_ENABLED = False

