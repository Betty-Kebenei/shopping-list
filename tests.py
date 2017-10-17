import unittest
from app import app
from app.models import User, users, Shopping_list, shopping_list

class TestBase(unittest.TestCase):
    """Class where configurations are passed."""

    def setUp(self):
        """A method that is passed before any test."""

        app.config["Testing"] = True


class ViewsTesting(TestBase):
    """This class represents tests on whether the pages load."""

    def test_signup_page_loads(self):
        """Test if signup page loads """

        res = app.test_client(self)
        response = res.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(u"Are you already signed up?", response.data)

    def test_signin_page_loads(self):
        """Test if signin page loads """

        res = app.test_client(self)
        response = res.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(u"Don't have an account?", response.data)

    def test_dashboard_page_loads(self):
        """Test if dashboard page loads """

        with app.test_client(self) as res:
            with res.session_transaction() as sess:
                sess["logged_in"] = True
        response = res.get('/dashboard', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(u"Welcome to shopping list tracker", response.data)

    def test_dashboard_fails(self):
        """Test if one must have a session to access the dashboard page. """

        res = app.test_client(self)
        with self.assertRaises(KeyError):
            res.get('/dashboard', content_type='html/text')

    def test_shoppingitems_page_loads(self):
        """Test if shopping items page loads """

        with app.test_client(self) as res:
            with res.session_transaction() as sess:
                sess["logged_in"] = True
        response = res.get('/shopping_items', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(u"Item Name", response.data)

    def test_shoppingitems_fails(self):
        """Test if one must have a session to access shopping items page. """

        res = app.test_client(self)
        with self.assertRaises(KeyError):
            res.get('/shopping_items', content_type='html/text')

    def test_logout(self):
        """Test if a user can log out."""

        res = app.test_client(self)
        response = res.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            u"Please enter your details to sign in into your 'shopping list account'.", response.data)


class FormdataTesting(TestBase):
    """This class represents the test cases on form data."""

    #### HELPER METHODS ###
    def signup(self, firstname, lastname, username, email, password, con_password):
        """Signup helper method."""

        res = app.test_client(self)
        return res.post('/signup', data=dict(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=email,
            password=password,
            con_password=con_password), follow_redirects=True)

    def login(self, email, password):
        """Login helper method"""

        res = app.test_client(self)
        return res.post('/login', data=dict(
            email=email,
            password=password), follow_redirects=True)

    def addlist(self, listname):
        """Creation of shopping list helper method"""

        with app.test_client(self) as res:
            with res.session_transaction() as sess:
                sess["logged_in"] = True
        return res.post('/shop_list', data=dict(listname=listname), follow_redirects=True)

    def additem(self, itemname, quantity, price):
        """Creation of shopping item helper method"""
        
        with app.test_client(self) as res:
            with res.session_transaction() as sess:
                sess["logged_in"] = True
        return res.post('/add_item', data=dict(
            itemname=itemname,
            quantity=quantity,
            price=price), follow_redirects=True)

    ### END OF HELPER METHODS ###
    
    def test_signup(self):
        """Test if signup is successful """

        response = self.signup("Betty", "Kebenei", "Bk1", "kebz@gmail.com", "123456A", "123456A")
        self.assertEqual(response.status_code, 200)

    def test_password_match(self):
        """Test if different passwords raises an error."""

        response = self.signup("Betty", "Kebenei", "Bk1", "kebz@gmail.com", "123456A", "aaaaa")
        self.assertIn(u"Your passwords should match.", response.data)
        
    def test_firstname_validation(self):
        """Test first name validation."""
        
        response = self.signup("B", "Kebenei", "Bk1", "kebz@gmail.com", "123456A", "123456A")
        self.assertIn(u"Field must be between 3 and 25 characters long.", response.data) 

    def test_lastname_validation(self):
        """Test last name validation."""

        response = self.signup("Betty", "", "Bk1", "kebz@gmail.com", "123456A", "123456A")
        self.assertIn(u"This field is required.", response.data)

    def test_username_validation(self):
        """Test user name validation."""

        response = self.signup("Betty", "Kebenei", "Bk", "kebz@gmail.com", "123456A", "123456A")
        self.assertIn(
            u"Field must be between 3 and 25 characters long.", response.data)

    def test_email_validation(self):
        """Test email validation."""

        response = self.signup("Betty", "", "Bk1", "kebz", "123456A", "123456A")
        self.assertIn(u"Invalid email address.", response.data)

    def test_login(self):
        """Test if login is successful"""

        response = self.login("kebz@gmail.com", "123456A")
        self.assertTrue(response.status_code, 200)

    def test_shoppinglist_creation(self):
        """Test creation of a shoppinglist"""

        self.signup("Betty", "Kebenei", "Bk1", "kebz@gmail.com", "123456A", "123456A")
        self.login("kebz@gmail.com", "123456A")
        response = self.addlist("books")
        self.assertEqual(response.status_code, 200)

    def test_list_creation_fails(self):
        """Test creation of a shoppinglist fails if one is not signed up and logged in"""

        res = app.test_client(self)
        with self.assertRaises(KeyError):
            res.post('/shop_list', data=dict(listname="books"), follow_redirects=True)

    def test_creation_validation(self):
        """A name consisting of @!#$%^ and other characters cannot make a shoppinglist name"""

        self.signup("Betty", "Kebenei", "Bk1", "kebz@gmail.com", "123456A", "123456A")
        self.login("kebz@gmail.com", "123456A")
        response = self.addlist("@@@@")
        self.assertNotIn(u"@@@@", response.data)

    def test_shoppingitems_creation(self):
        """Test creation of an item in the shopping list"""

        self.signup("Betty", "Kebenei", "Bk1", "kebz@gmail.com", "123456A", "123456A")
        self.login("kebz@gmail.com", "123456A")
        self.addlist("books")
        response = self.additem("Python", 1, 3000)
        self.assertEqual(response.status_code, 200)

    def test_item_creation_fails(self):
        """Test adding of a shopping item fails if one is not logged in"""

        res = app.test_client(self)
        with self.assertRaises(KeyError):
            res.post('/add_item', data=dict(
            itemname="Python",
            quantity=1,
            price=3000), follow_redirects=True)

class ModelsTesting(TestBase):
    """This class tests if list can be appended and deleted from."""

    def test_user_added(self):
        """Testing addition of a user to a list of users."""
        
        user = User("Betty", "Kebenei", "Berry", "kebeneibetty13@gmail.com", "123456A")
        users.append(user)
        self.assertEqual(1, len(users))

    def test_shoppinglist_added(self):
        """Testing addition of a shopping list to a list of shopping lists."""

        books = Shopping_list("Books")
        shopping_list.append(books)
        self.assertEqual(1, len(shopping_list))

    def test_shoppinglist_deleted(self):
        """Testing deletion of a shopping list from a list of shopping lists."""

        bags = Shopping_list("Bags")
        shopping_list.append(bags)
        self.assertEqual(2, len(shopping_list))
        shopping_list.remove(bags)
        self.assertEqual(1, len(shopping_list))      

if __name__ == '__main__':
    unittest.main()
