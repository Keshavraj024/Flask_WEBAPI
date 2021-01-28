#Import the modules
from flask import abort,redirect,url_for
import secrets,time

class Payment:
	def __init__(self):
		self.Payment_mode = {"Service_1":"CheapPayment","Service_2":"ExpensivePayment","Service_3":"PremiumPayment"}
		self.num_of_attempts = {'counter':0}
		self.tokens = []
			
	#Generate the secret tokens
	def generate_token(self):
		token = secrets.token_bytes(16)
		return token

	#Function to handle the Payment Gateway
	def payment(self,amount,form=None):
		#Function to handle the form Errors
		if form.errors:

			#If the amount is negative
			if (amount < 0):
				redirect(url_for('views.credit_card_form'))
			
			#Aborts if form error exists and the amount is less than 20
			# elif (amount <= 20):
			# 	abort(400)
			
			#Aborts if form error exists and the amount is between than 20 and 500
			elif amount > 20 and amount <= 500:
				abort(400)
			
			#Retries for consecutive three times and if the error 
			#exists then abort
			elif amount > 500:
				if self.num_of_attempts['counter'] >= 3:
					self.num_of_attempts['counter'] = 0
					abort(400)

				#Stays on the same page for three attempts
				redirect(url_for('views.credit_card_form'))
				self.num_of_attempts['counter'] += 1

		#Handles the form with no errors
		else:
			# Expensive Payment Transaction and to check the server swam
			if amount > 20 and amount < 500:
				'''
				Server holds on the same page for certain duration
				just to make the server busy and check 
				server availability from other new session
				If not need just comment out the time.sleep() method
				'''
				self.tokens.append(self.generate_token())
				if len(self.tokens) == 1:
					time.sleep(10)
					self.tokens.clear()
					return self.Payment_mode['Service_2']
				# If the server is busy redirects to Cheap Payment Transaction
				else:
					if self.tokens[0] != self.tokens[1]:
						return self.Payment_mode['Service_1']

			#Cheap Payment Transaction
			elif amount < 20:
				return self.Payment_mode['Service_1']

			#Premium Payment Transaction
			else:
				return self.Payment_mode['Service_3']
		
			
		

		


