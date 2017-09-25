import random

users=[]
shopping_list=[]
shopping_items=[]
class User(object):
    
    def __init__(self,first_name,last_name,username,email,password):
        self.id_number=random.randrange(1,1000,1)
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.email=email
        self.password=password


class Shopping_list(object):
    def __init__(self,listname):
        self.id_number=random.randrange(1,1000,1) #number of the shopping_list
        #self.owner=owner    #owner of the shopping list
        self.listname=listname


class Shopping_items(object):
    def __init__(self,itemname,quantity,price):
        self.itemname=itemname
        self.quantity=quantity
        self.price=price
       
    #def add_shopping_item(self):

    def view_shopping_items(self):
        return shopping_items

    #def update_shopping_item(self):

    def delete_shopping_item(self):
        if item_to_delete in Shopping_items:
            shopping_items.remove(item_to_delete)
            return "Item deleted."    
