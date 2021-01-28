# Import the modules
from flask_wtf import FlaskForm
from wtforms import HiddenField,StringField,SubmitField,IntegerField,DateTimeField,DecimalField
from wtforms.validators import DataRequired,Length,ValidationError,Optional
from cardvalidator import luhn
import datetime
from flask import request,render_template


#Class to create the form with necessary fields
class CreditCardForm(FlaskForm):
	CreditCardNumber = StringField('CreditCardNumber',
							validators=[DataRequired()])
	CardHolder = StringField('CardHolder',validators=[DataRequired()])
	ExpirationDate = DateTimeField('ExpirationDate (Y/M/D)',format="%Y/%m/%d",validators=[DataRequired()])
	SecurityCode = IntegerField('SecurityCode',[Optional()])
	Amount = DecimalField('Amount',[DataRequired()])
	Test = HiddenField('Test',[Optional()])
	submit = SubmitField('Submit')

	#Validate the Credit Card Number
	def validate_CreditCardNumber(self,CreditCardNumber):
		if not luhn.is_valid(self.CreditCardNumber.data):
			#Reset the field if error exists
			self.CreditCardNumber.data = ""
			raise ValidationError("Invalid Credit Card Credentials") 

	#Validate the CardHolder
	def validate_CardHolder(self,CardHolder):
		if not(self.CardHolder.data).isalpha():
			#Reset the field if error exists
			self.CardHolder.data = ""
			raise ValidationError("Invalid User Name.Username should be in String")
		
	#Validate the ExpirationDate
	def validate_ExpirationDate(self,ExpirationDate):

		if not(isinstance(self.ExpirationDate.data, datetime.datetime)):
			#Reset the field if error exists
			self.ExpirationDate.raw_data = ['']
			raise ValidationError("Alphabets or Special Characters are not allowed")

		elif not(self.ExpirationDate.data) > datetime.datetime.now():
			#Reset the field if error exists
			self.ExpirationDate.raw_data = ['']
			raise ValidationError("Invalid Expiration Date Specified")
		
	#Validate the SecurityCode
	def validate_SecurityCode(self,SecurityCode):
		if len(str(self.SecurityCode.data)) < 3 or len(str(self.SecurityCode.data)) > 3:
			#Reset the field if error exists
			self.SecurityCode.raw_data = ['']
			raise ValidationError('SecurityCode must be equal to 3 digits')

	#Validate the Amount
	def validate_Amount(self,Amount):
		if self.Amount.data < 0 :
			#Reset the field if error exists
			self.Amount.raw_data = [""]
			raise ValidationError("Amount should be Positive")
