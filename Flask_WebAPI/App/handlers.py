#Blueprint to handle the errors

from flask import Blueprint,render_template

errors = Blueprint('handlers', __name__)

#Handles Bad Request from Client End
@errors.app_errorhandler(400)
def error_400(error):
	return render_template("400.html",title="Error"),400

#Handles inappropriate routes
@errors.app_errorhandler(404)
def error_404(error):
	return render_template("404.html",title="Error"),404

#Handles Internal Server Error
@errors.app_errorhandler(500)
def error_500(error):
	return render_template("500.html",title="Error"),500
