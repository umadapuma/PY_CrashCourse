#7-4 Pizza Toppings:
prompt = '\nWhat toppings would you like on your pizza?'
prompt += ("\nEnter 'quit' to stop adding toppings.")
toppings = ""
while toppings != 'quit':
    toppings = input(prompt)
    print(toppings)

print('-------------------------------')
#7-5 Movie Tickets:
prompt = "\nPlease enter your age:"

while True:
    age = input(prompt)
    age = int(age)
    if age<=3:
        print('Your ticket is free')
        break
    if 3<age<=12:
        print('Your ticket is $10')
        break
    if age>12:
        print('Your ticket is $15')
        break
#7-6 Three Exits:
x = 1
toppings = ""
while x <= 5:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    print(toppings)
    

#7-7
while True:
    print('make it stop')