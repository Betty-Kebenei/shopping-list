import random

users=[]
class User(object):
    
    def __init__(self,first_name,last_name,username,email,password):
        self.id_number=random.randrange(1,1000,1)
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.email=email
        self.password=password

    def login(self):
        if users.get(self.email):
            if users[self.email] == self.password:
                return "Logged in successfully"
            return "Wrong Password"
        return "You are not registered"
  

#class Shopping_list(object):
   # def __init__(self,id_number,owner):
        #self.id_number=id_number #number of the shopping_list
        #self.owner=owner    #owner of the shopping list
    
    #def create_shopping_list(self):

    #def update_shopping_list(self):

    #def delete_shopping_list(self):

#class Shopping_items(object):
    #def __init__(self,list):
        #self.list=list
       
    #def add_shopping_item(self):

    #def update_shopping_update(self):

    #def delete_shopping_delete(self):    
