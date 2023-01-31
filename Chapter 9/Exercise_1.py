#9-1 Restaurant:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant('SuperYum','American')
print(f"The restaurant we went to was {restaurant.restaurant_name}.")
print(f"{restaurant.restaurant_name} had {restaurant.cuisine_type} food.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2 Three Restaurants: 
tacobell = Restaurant("Taco Bell","Tex-Mex")
chickfila = Restaurant("Chick Fil A",'Chicken Sammies')
dirtstore = Restaurant("Dirtstore","Dirt")
print('\n')
tacobell.describe_restaurant()
chickfila.describe_restaurant()
dirtstore.describe_restaurant()

print('\n')
#9-3 Users:
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        print(f"Nice to meet you {self.first_name} {self.last_name}")
        print('\n')

bobert = User("Robert","Bobbert")
bobert.describe_user()
bobert.greet_user()

dilbert = User('Dilbert','Philbert')
dilbert.describe_user()
dilbert.greet_user()

knawber = User('Knawber','Dawber')
knawber.describe_user()
knawber.greet_user()