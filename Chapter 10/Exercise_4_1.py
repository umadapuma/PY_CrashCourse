import json
filename = 'user_number.json'
try:
    with open(filename) as f:
        user_num = json.load(f)
except FileNotFoundError:
    user_num = input("What is your favorite number?")
    json.dump(user_num,f)
    print(f"We will remember your favorite number is {user_num}.")
else:
    print(f"Your favorite number is {user_num}!")