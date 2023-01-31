#9-4 Number Served:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def amount(self):
        """Amount of people served at the restaurant"""
        print(f'{self.number_served} people served.')

    def set_number_served(self,customers):
        self.number_served = customers

    def increment_number_served(self,new_customers):
        self.number_served += new_customers

restaurant = Restaurant('SuperYum','American')
print(f"The restaurant we went to was {restaurant.restaurant_name}.")
print(f"{restaurant.restaurant_name} had {restaurant.cuisine_type} food.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.amount()
restaurant.number_served = 10
restaurant.amount()
restaurant.set_number_served(100)
restaurant.amount()
restaurant.increment_number_served(15)
restaurant.amount()

#9-5 Login Attempts:
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        print(f"Nice to meet you {self.first_name} {self.last_name}")
        print('\n')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

bobert = User("Robert","Bobbert")
bobert.describe_user()
bobert.greet_user()

dilbert = User('Dilbert','Philbert')
dilbert.describe_user()
dilbert.greet_user()

knawber = User('Knawber','Dawber')
knawber.describe_user()
knawber.greet_user()

checkford = User('Checkford', 'Checky')
checkford.describe_user()
checkford.increment_login_attempts()
checkford.increment_login_attempts()
checkford.increment_login_attempts()
checkford.increment_login_attempts()

print(f'{checkford.login_attempts}')

checkford.reset_login_attempts()
print(f'{checkford.login_attempts}')