age = 65

if age < 2:
    print('your a baby')
elif age>=2 and age < 4:
    print('toddler')
elif age>=4 and age<13:
    print('kid')
elif age>=13 and age<20:
    print('teenager')
elif age>=20 and age<65:
    print('adult')
else:
    print('elder')
print('--------------------------------')
#5-7
favorite_fruits = ['grapes','pear','apple']

if 'banana' in favorite_fruits:
    print('you like bananas')
if 'grapes' in favorite_fruits:
    print('you like grapes')
if 'orange' not in favorite_fruits:
    print("You don't like oranges")
if 'pear' or 'apple' in favorite_fruits:
    print('You like fruits with seeds in them')
    
    if 'dragonfruit' not in favorite_fruits:
        print('you should try dragonfruit, its packed with seeds')