#9-6 Ice Cream Stand:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
class IceCreamStand(Restaurant):
    def __init__(self, restauraunt_name,cusine_type):

        super().__init__(restauraunt_name,cusine_type)
        self.flavors = ['chocolate','vanilla','strawberry']

    def listflavors(self):
        print(f'The flavors available include:\n')
        for flavor in self.flavors:
            print(flavor)
yummietreat = IceCreamStand('Yummie Treat','Ice Cream')
yummietreat.listflavors()

#9-7 Admin:
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
print('\n')
#9-8 Privileges:
class Privileges:
    def __init__(self):
        self.privileges = ['can add post','can delete post', 'can ban user']
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
        
testing = Admin("Les","Paul")
testing.privileges.show_privileges()

#9-9 Battery Upgrade:

class Car:
     # A simple attempt to represent a car.
     def __init__(self, make, model, year):
         # Initialize attributes to describe a car.
         self.make = make
         self.model = model
         self.year = year
         self.odometer_reading = 0

     def get_descriptive_name(self):
         # Return a neatly formatted descriptive name.
         long_name = str(self.year) + " " + self.make + " " + self.model
         return long_name.title()

     def read_odometer(self):
         # Print a statement showing the car's mileage.
         print("This cas has " + str(self.odometer_reading) + " miles on it.")

     def update_odometer(self, mileage):
         # Set the odometer reading to the given value.
         # Reject the change if it attempts to roll the odometer back.
         if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
         else:
             print("You can't roll back an odometer!")

     def increment_odometer(self, miles):
         # Add the given amount to the odometer reading.
         self.odometer_reading += miles

     def fill_gas_tank(self):
         print("This car needs a gas tank!")

class Battery:
    # A simple attempt to model a battery for an electric car.
    def __init__(self, battery_size=70):
        # Initialize the battery's attributes.
        self.battery_size = battery_size

    def describe_battery(self):
        # Print a statement describing the battery size.
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        # Print a statement about the range this battery provides.
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 100:
            range = 270

        message = "This car can go approximately " + str(range) + \
                  " miles on a full charge."
        print(message)
        
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar(Car):
    # Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        # Initialize attributes of the parent class.
        # Then initialize attributes specific to an electric car.
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()

    # def describe_battery(self):
    #     # Print a statement describing the battery size.
    #     print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        # Electric cars don't have gas tanks.
        print("This car doesn\'t need a gas tank!")

fastcar = ElectricCar("Nisin","Chargo","2077")
fastcar.battery.get_range()
fastcar.battery.upgrade_battery()
fastcar.battery.get_range()