#10-11 Favorite Number:
import json
user_number = input("What is you favorite number? ")

filename = 'user_number.json'


filename = 'fav_numbers.json'
with open(filename, 'w') as f:
    json.dump(user_number,f)

#10-12 Favorite Number Remembered:
try:
    with open(filename) as f:
        user_num = json.load(f)
except FileNotFoundError:
    user_num = input("What is your favorite number?")
    json.dump(user_num,f)
    print(f"We will remember your favorite number is {user_num}.")
else:
    print(f"Your favorite number is {user_num}!")

