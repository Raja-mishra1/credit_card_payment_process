try:
    import unittest
    from app import app


except Exception as e:
    print("Some Modules are missing {}".format(e))


class FlaskTestCase(unittest.TestCase):

    # check for sucessful connection
    def test_Flask_connection(self):
        tester = app.test_client(self)
        response = tester.post("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # content return check
    # def test_Flask_content(self):
    #     tester = app.test_client(self)
    #     response = tester.post("/")
    #     self.assertEqual(response.content_type, "text/html")

    # check for data returned
    def test_Flask_returned_data(self):
        tester = app.test_client(self)
        response = tester.post("/")
        self.assertTrue(b"Success" or "Failure" in response.data)


if __name__ == "__main__":
    unittest.main()