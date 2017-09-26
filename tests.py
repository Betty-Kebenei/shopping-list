import unittest
from flask import Flask, url_for
from app import app 

class Test(unittest.TestCase):

    def create_app(self):
       app = Flask(__name__)
       app.config['TESTING'] = True

    def test_signup_page_loads(self):
        sampletest = app.test_client(self)
        response = sampletest.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
        unittest.main()