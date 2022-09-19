#5-1
circle = 'circle'
square = 'square'
print('I predict the circle is a circle to be True')
print( circle == 'circle')
print('I predict the circle is square to be False')
print(circle == 'square')
print('I predict the cicle is a Circle to be False')
print(circle == 'Circle')
print('I predict the circle is a Circle when change to .lower to be True')
print(circle == 'Circle'.lower())
print('I predict a circle not equal to triangle will be True')
print(circle != 'triangle')
print('I predict a circle not equal to circle will be False')
print(circle != 'circle')
print('I predict circle is a circle and square is a triangle will be False')
print((circle == 'circle') & (square == 'triangle'))
print('I predict that circle is a circle or square is a triangle will be True')
print((circle =='circle' or square == 'triangle'))

#5-2
types_of_phones = ['iphone','androi']

if 'iPhone'.lower() in types_of_phones:
    print('the iphone is in the list')

if 'Windows'.lower() not in types_of_phones:
    print('Windows phone not in the list')