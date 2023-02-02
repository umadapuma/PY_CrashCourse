#9-13 Dice:
from random import randint
from random import choice
class Die:
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))
die6 = Die()
die10 = Die(10)
die20 = Die(20)
for x in range(10):
    print('\t')
    die6.roll_die()
    die10.roll_die()
    die20.roll_die()

#9-14 Lottery:
numbers_letters=(23,34,65,2,78,13,76,48,93,50,'r','s','u','v','q')
lottery = []
for x in range(4):
    lottery.append(choice(numbers_letters))
print(lottery)
print('Any tickets matching the following four numbers/letters ' + str(lottery) + ' wins a prize')

#9-15 Lottery Analysis:
my_ticket = []
flag =0
while lottery != my_ticket:
    flag += 1
    my_ticket.clear()
    for x in range(4):
        my_ticket.append(choice(numbers_letters))
    print(str(my_ticket) + str(flag))

print(lottery)