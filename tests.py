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
        response = res.post('/signup', data=dict(firstname="firstname", lastname="lastname", username="username",
                                                    email="hey@gmail.com", password="123"), 
                                                    follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_passes(self):
        """Ensuring that login passes as expected"""

        res = app.test_client(self)
        response = res.post('/login', data = dict(username="hey@gmail.com", password="123"),
                                    follow_redirects=True)
        self.assertTrue('Welcome' in response.data)

class ShoppinglistsTestCase(unittest.TestCase):
    """This class represents the shopping list test cases"""

    def test_dashboard_page_loads(self):
        """Test if signup page loads """

        res = app.test_client(self)
        response = res.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_shoppinglist_creation(self):
        """Test creation of a shoppinglist"""

        res = app.test_client(self)
        res.post('/signup', data=dict(firstname="firstname", lastname="lastname", username="username",
                                                    email="hey@gmail.com", password="123"), 
                                                    follow_redirects=True)
        res.post('/login', data = dict(username="hey@gmail.com", password="123"),
                                    follow_redirects=True)
        response = res.post('/shop_list', data=dict(listname="books"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_shoppinglist_deletion(self):
        """Test deletion of a shoppinglist """

        res = app.test_client(self)
        res.post('/signup', data=dict(firstname="firstname", lastname="lastname", username="username",
                                                    email="hey@gmail.com", password="123"), 
                                                    follow_redirects=True)
        res.post('/login', data = dict(username="hey@gmail.com", password="123"),
                                    follow_redirects=True)
        res.post('/shop_list', data=dict(listname="books"), follow_redirects=True)
        response = res.post('/shop_list', data=dict(listname="books"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class ShoppingItemsTestCase(unittest.TestCase):  
    """This class represents the shopping items test cases"""  

    def test_shoppingitems_page_loads(self):
        """Test if the page used to add shopping items loads """

        res = app.test_client(self)
        response = res.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_shoppingitems_creation(self):
        """Test creation of an item in the shopping list"""

        res = app.test_client(self)
        res.post('/signup', data=dict(firstname="firstname", lastname="lastname", username="username",
                                                    email="hey@gmail.com", password="123"), 
                                                    follow_redirects=True)
        res.post('/login', data = dict(username="hey@gmail.com", password="123"),
                                    follow_redirects=True)
        res.post('/shop_list', data=dict(listname="books"), follow_redirects=True)
        response = res.post('/shop_item', data=dict(itemname='itemname', quantity='quantity', price='price'), 
                                                        follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()