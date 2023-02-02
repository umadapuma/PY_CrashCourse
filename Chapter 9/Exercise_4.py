#9-10 Imported Restaurant:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

#    def greet_user(self):
 #       print(f"Nice to meet you {self.first_name} {self.last_name}")
  #      print('\n')

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        #self.privileges = ['can add post','can delete post', 'can ban user']
        self.privileges = Privileges()
    
#    def show_privileges(self):
 #       for privilege in self.privileges:
 #           print(privilege)

#boss = Admin('Bob',"Barker")
#boss.show_privileges()
#print('\n')
#9-8 Privileges:
class Privileges:
    def __init__(self):
        self.privileges = ['can add post','can delete post', 'can ban user']
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
        
#esting = Admin("Les","Paul")
#testing.privileges.show_privileges()