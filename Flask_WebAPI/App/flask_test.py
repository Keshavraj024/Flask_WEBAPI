# Import the necessary Modules
from . import create_app
from .config import TestConfig
import unittest
import requests

# Flask Test Class
class FlaskTestCase(unittest.TestCase):

	# Prior Execution to each Test
	def setUp(self):
		app = create_app()
		app.config.from_object(TestConfig)
		self.app = app.test_client()

	# Executed after each Test
	def tearDown(self):
        # Perform tear down after each test, using app
		pass
    
	# Helper Methods to perform future tests
	def ProcessPayment(self,CreditCardNumber,CardHolder,ExpirationDate,SecurityCode,Amount,Test):
		return self.app.post('/ProcessPayment',data=dict(CreditCardNumber=CreditCardNumber,CardHolder=CardHolder,ExpirationDate=ExpirationDate,SecurityCode=SecurityCode,Amount=Amount,Test=Test),follow_redirects=True)
	
	# Perform Tests
	# Check whether server is running
	def test_server_run(self):
		response = requests.get('http://127.0.0.1:5000/ProcessPayment')
		self.assertEqual(response.status_code,200)
	
	# Testing data availability in the request Payload
	def test_no_data(self):
		response = self.ProcessPayment(None,None,None,None,None,"Test")
		#print(response.data)
		self.assertTrue(response)	

	# Testing CreditCardNumber in the request Payload
	def test_invalid_CreditCardNumber_entry(self):
		response = self.ProcessPayment("992405734","Keshav",'2027/7/8','111',int(222.2),"Test")
		self.assertEqual(response.status_code, 400)

	# Testing CardHolder in the request Payload
	def test_invalid_CardHolder_entry(self):
		response = self.ProcessPayment("9924192924205734","Keshav123",'2027/7/8','111',int(222.2),"Test")
		self.assertEqual(response.status_code, 400)

	# Testing ExpirationDate in the request Payload
	def test_invalid_ExpirationDate_entry(self):
		response = self.ProcessPayment("9924192924205734","Keshav",'2020/7/8','111',int(222.2),"Test")
		self.assertEqual(response.status_code, 400)
	
	# Testing SecurityCode in the request Payload
	def test_invalid_SecurityCode_entry(self):
		response = self.ProcessPayment("9924192924205734","Keshav",'2027/7/8','11',int(222.2),"Test")
		self.assertEqual(response.status_code, 400)
	
	# Testing Amount in the request Payload
	def test_invalid_Amount_entry(self):
		response = self.ProcessPayment("9924192924205734","Keshav",'2027/7/8','111',-222.2,"Test")
		self.assertEqual(response.status_code, 400)
	
	
	# Test availability of mandatory missing field
	def test_missing_mandatory_field(self):
		response = self.app.post('/ProcessPayment',data=dict(Amount=100,Test="Test"),follow_redirects=True)
		self.assertEqual(response.status_code, 400)

	# Testing Valid data in the request Payload
	def test_valid__entries(self):
		response = self.ProcessPayment("9924192924205734","Keshav",'2027/7/8','111',int(222.2),"Test")
		self.assertEqual(response.status_code, 200)

	# Test availability of optional missing field
	def test_missing_optional_field(self):
		response = self.app.post('/ProcessPayment',data=dict(CreditCardNumber="9924192924205734",ExpirationDate='2027/7/8',SecurityCode='111',Amount=222.2,CardHolder="Keshav",Test="Test"),follow_redirects=True)
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()










# @pytest.fixture(scope='module')
# def test_client():
#     app = Flask(__name__)
# 	# app = create_app(config_class = TestConfig)
#     flask_app =app.config.from_object('TestConfig')
 
#     # Flask provides a way to test your application by exposing the Werkzeug test Client
#     # and handling the context locals for you.
#     testing_client = flask_app.test_client()
 
#     # Establish an application context before running the tests.
#     ctx = flask_app.app_context()
#     ctx.push()
 
#     yield testing_client  # this is where the testing happens!
 
#     ctx.pop()

# def test_home_page(test_client):
#     """
#     GIVEN a Flask application
#     WHEN the '/' page is requested (GET)
#     THEN check the response is valid
#     """
#     card_data = dict(CreditCardNumber="4766433000569581", CardHolder="Keshav", ExpirationDate='2021/7/8',SecurityCode='111',Amount=int(222.2))
#     response = test_client.get('/ProcessPayment', data=card_data)
# 	#print(response.text)
#     assert response.status_code == 200







# class configure:
# 	def a(self):
# 		app = Flask(__name__)
# 		# app = create_app(config_class = TestConfig)
# 		app.config.from_object(TestConfig)
# 		print(self.app.config["WTF_CSRF_ENABLED"])
# 		print("Hello")
# 		return app
		
# class Test:
# 	def test_invalid_request_type(self):
# 		#print(c)
# 		#print(app.config["WTF_CSRF_ENABLED"])
# 		s = configure()
# 		print(s.a())
# 		response = requests.get(f"http://{s.a.config['FLASK_RUN_HOST']}:{config['FLASK_RUN_PORT']}/ProcessPayment")
# 		assert response.status_code == 200

# def test_invalid_data(config):
# 	card_data = dict(CreditCardNumber="4766433000569581", CardHolder="Keshav", ExpirationDate='2021/7/8',SecurityCode='111',Amount=int(222.2))
# 	response = requests.post(f"http://{app.config['FLASK_RUN_HOST']}:{app.config['FLASK_RUN_PORT']}/ProcessPayment", data=card_data)
# 	print(response.text)
# 	assert response.status_code == 200

# c = configure()
# test_invalid_request_type(configure=c)