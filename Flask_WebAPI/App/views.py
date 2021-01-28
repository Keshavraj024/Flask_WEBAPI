#Import the necessary modules
from flask import Blueprint,abort,render_template,redirect,url_for,request
from .forms import CreditCardForm
from .external import Payment
from datetime import timedelta,datetime
import time

sessions =dict(timeout=0)
#Creates the Payment Object
pay = Payment()
view = Blueprint("views", __name__,static_folder="static",template_folder="templates")
names = ["CheapPayment","ExpensivePayment","PremiumPayment"]


#Handles the home route
@view.route('/')
@view.route("/<name>/<session>")
def home(name=None,session=None):
	#Redirects the session to the Process Payment if session terminates
	if (int(round(time.time() * 1000)) - sessions['timeout']) >= 3000:
		return redirect(url_for('views.credit_card_form'))
	
	elif name in names:
		#Render the home template if session exists
		sessions['timeout'] = int(round(time.time() * 1000))
		return render_template("home.html",title='Home',name=name,session=sessions['timeout'])
		
	else:
		abort(404)  

#Handles the Process Payment Route
@view.route("/ProcessPayment",methods=['GET','POST'])
def credit_card_form():
	#Create the CreditCardFormObject
	form = CreditCardForm()
	
	#Validates the form on Submit and redirects to Output Page
	if request.method == 'POST' and form.validate_on_submit():
		name = pay.payment(amount=float(request.form['Amount']),form=form)
		sessions['timeout'] = int(round(time.time() * 1000))
		return redirect(url_for('views.home',name=name,session=sessions['timeout']))
	
	#Handles the form errors
	elif form.errors:
		#Handles the Unit tests functionality
		if request.form['Test']:
			abort(400)
		#Redirects to retry the payment in case of errors
		pay.payment(amount=float(request.form['Amount']),form=form)
		
	return render_template("payment.html",title="Payment",form=form)
	
