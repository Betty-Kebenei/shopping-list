import unittest
from flask import Flask, url_for
from app import app 

class UserTestCase(unittest.TestCase):
    """This class represents the user test cases"""

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

    def test_signup_page_loads(self):
        """Test if signup page loads """

        res = app.test_client(self)
        response = res.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup_successful(self):
        res = app.test_client(self)
        response = res.post('/signup', users=(firstname="firstname", lastname="lastname", username="username", email="email", password="password", con_password="con_password") follow_redirects=True)
        self.assertTrue('email' in response.data)

    def test_login_passes(self):
        """Ensuring that login passes as expected"""

        res = app.test_client(self)
        response = res.post('/login', data(username="email", password="password"),
                                   follow_redirects=True)
        self.assertTrue('account' in response.data)

class ShoppinglistsTestCase(unittest.TestCase):
    """This class represents the shopping list test cases"""

    def test_dashboard_page_loads(self):
        """Test if signup page loads """

        res = app.test_client(self)
        response = res.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_shoppinglist_creation(self):
        """Test creation of a shoppinglist (POST request)"""

        res = app.test_client(self)
        response = res.post('/shop_list/', data=self.shop_list)
        self.assertEqual(res.status_code, 201)


class ShoppingItemsTestCase(unittest.TestCase):  
    """This class represents the shopping items test cases"""  

if __name__ == '__main__':
    unittest.main()