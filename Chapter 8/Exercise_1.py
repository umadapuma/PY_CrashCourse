#8-1 Messages:
from itertools import count


def display_message():
    print("This chapter I am learning about functions.")

display_message()

#8-2 Favorite Book:
def favorite_book(title):
    print('One of my favorite books is ' + title.title() + '.')
favorite_book('alice in wonderland')

#8-3 T-Shirt:
def make_shirt(size,text):
    print("\nSize: "+ size + '\nText: '+ text)
make_shirt('XL',"Money back Gaurantee")
make_shirt(text = 'Bob the Builder', size = 'L')
print('-------------------------------------')
#8-4 Large Shirts:
def make_shirt(text='i love python', size='l'):
    print('\nSize: ' + size.capitalize())
    print("Text: " + text.title())

make_shirt()
make_shirt(size = 'm')
make_shirt("Discotecha")
print("------------------------------")
#8-5 Cities:
def describe_city(city, country='USA'):
    print(city.title() + " is in " + country.title())

describe_city('seattle')
describe_city('mexico city','mexico')
describe_city(country='canada',city='montreal')