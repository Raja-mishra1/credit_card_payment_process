try:
    import unittest
    from app import app
    import requests
    from datetime import datetime


except Exception as e:
    print("Some Modules are missing {}".format(e))


class FlaskTestCase(unittest.TestCase):
    API_URL = "http://0.0.0.0:5000/api/v1/payments/"
    date = datetime.strptime("20201231", "%Y%m%d")

    # testcases data with valid transaction details
    data = {
        "CreditCardNumber": "354673100235957",
        "CardHolder": "John",
        "ExpirationDate": datetime.strftime(date, "%m/%d/%Y"),
        "SecurityCode": "CVV",
        "Amount": 100.70,
    }
    # testcases data with invalid transaction details
    failure_data = {
        "CreditCardNumber": "12345",
        "CardHolder": "John",
        "ExpirationDate": datetime.strftime(date, "%m/%d/%Y"),
        "SecurityCode": "CVV",
        "Amount": 100,
    }

    # succesfull transaction , checking code
    def test_Flask_post_data(self):
        response = requests.post(FlaskTestCase.API_URL, json=FlaskTestCase.data)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #successful transaction , checking response
    def test_Flask_returned_data(self):
        response = requests.post(FlaskTestCase.API_URL, json=FlaskTestCase.data)
        self.assertTrue(b"OK" in response)

    #failed transaction 
    def test_Flask_returned_data_failure(self):
        response = requests.post(FlaskTestCase.API_URL, json=FlaskTestCase.failure_data)
        self.assertTrue(b"Internal Server Error" or "Bad Request" in response)


if __name__ == "__main__":
    unittest.main()
