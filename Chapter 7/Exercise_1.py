#7-1 Rental Car
car = input('What kind of rental car would you like? ')
print("Let me see if I can find you a " + car)

#7-2 Resturant Seating
pplCount = input('How may people will be dining today? ')

if(int(pplCount) > 8):
    print('You will have to wait for a table.')
else:
    print('Your table is ready.')

#7-3 Multiples of Ten:
number=input('Think of a number and tell me it ')
number =int(number)

if number %10 ==0:
    print('Your number is a multiple of 10')
else:
    print('Your number is not a multiple of 10')

