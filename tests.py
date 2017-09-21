import unittest
from app import app 

class Test(unittest.TestCase):

    def test_signup_page_loads(self):
        sampletest = app.test_client(self)
        response = sampletest.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_reg(self):
        sampletest = app.test_client(self)
        response = sampletest.post('/signup', data=list(first_name="bety",
                                                        last_name="keb",
                                                        username="bk",
                                                        email="kb@gmail.com",
                                                        password="123"),                                                        
                                   follow_redirects=True)
        self.assertTrue('Please' in response.data)
    
    def test_list_create(self):
        sampletest = app.test_client(self)
        response = sampletest.post('/shop_list', data=list(list_name="one"),                                                        
                                   follow_redirects=True)
        self.assertTrue('Welcome' in response.data)







if __name__ == '__main__':
        unittest.main()