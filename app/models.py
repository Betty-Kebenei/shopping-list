import random
users = []
shopping_list = []

class User(object): 
    """This class represents the users class."""

    def __init__(self, first_name, last_name, username, email, password):
        self.id_number = random.randrange(1, 1000, 1)
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

class Shopping_list(User):
    """This class represents the shopping list class."""

    def __init__(self, listname, created_by):  # add created_by argument
        self.list_id = random.randrange(1, 1000, 1) 
        self.listname = listname
        self.shopping_items = []
        self.created_by = created_by  # new attribute
  
class Shopping_items(Shopping_list):
    """This class represents the shopping items class."""

    def __init__(self, itemname, quantity, price):
        self.item_id = random.randrange(1, 1000, 1)
        self.itemname = itemname
        self.quantity = quantity
        self.price = price
