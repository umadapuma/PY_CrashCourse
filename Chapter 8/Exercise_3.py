#8-9 Magicians 
from hashlib import new


magicians = ['Bob','Bills','Mary','Dani']
great_magicians = magicians[:]
great_magicians2 = []

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians, magicians2):
    while magicians:
        new_magicians = "Great " + magicians.pop() 
        magicians2.append(new_magicians)
       # print(new_magicians)


#8-10 Great Magicians:

make_great(great_magicians,great_magicians2)
show_magicians(great_magicians2)

print('-------------------------------------')
#8-11 Unchanged Magicians:
show_magicians(magicians)
show_magicians(great_magicians2)