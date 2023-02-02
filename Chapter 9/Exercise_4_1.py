from Exercise_4 import Restaurant, Admin, Privileges,User

foodplace = Restaurant("Taco Bell","American-Mexican")
Restaurant.describe_restaurant(foodplace)

boss = Admin("Big","Bob")
boss.privileges.show_privileges()