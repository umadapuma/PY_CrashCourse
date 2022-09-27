#7-8 Deli:  #7-9 No Pastrami:
sandwich_orders=['pastrami','ruben','turkey','pastrami','philly cheesesteak','pb&j','pastrami']
finished_sandwiches=[]
print("The deli has run out of pastrami\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your ' + sandwich)
    finished_sandwiches.append(sandwich)

print('We made the following sammies')
for sammie in finished_sandwiches:
    print(sammie)

#7-10 Dream Vacation:
dreams = {}
polling_status = True

while polling_status:
    name = input("\nWhat is your name?")
    dream = input("Where would you travel?")

    dreams[name] = dream
    
    repeat = input("Is there anyone else taking the poll?")
    if repeat == 'no':
        polling_status = False
    
print('\n---Poll Results---')
for name, dream in dreams.items():
    print(name + ' would like to travel to '+dream+'.')



