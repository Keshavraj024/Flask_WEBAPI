#Import the necessary modules
from flask import Flask
from .views import view
from .config import ProdConfig
from .handlers import errors
from flask_wtf.csrf import CsrfProtect
csrf = CsrfProtect()

# Function to initialise the app
def create_app(config_class = ProdConfig):
	app = Flask(__name__)
	#Config using Production Env Configuration
	csrf.init_app(app)
	app.config.from_object(ProdConfig) 
	#Register the blueprints
	app.register_blueprint(view)	  
	app.register_blueprint(errors)
	#Return the app
	return app