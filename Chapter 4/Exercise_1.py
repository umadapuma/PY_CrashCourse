#4-1 Pizzas:
pizzas = ['pineapple', 'chicken', 'cheese']

for pizza in pizzas:
    print(f'I like {pizza}')
print('\nI freakin luv pizza!!\n')

#4-2 Animals:

animals = ['dog','cat','bird']

for animal in animals:
    print(f'A {animal} would make a great pet')
print('\nAny of these animals would make a great pet!\n')

print("------------------------------")

#4-11
friend_pizzas = pizzas[:]
pizzas.append('pepperoni')
friend_pizzas.append('mushroom')

print('my favorite pizzas include:')
for pizza in pizzas:
    print(pizza)

print('\nMy friends fav pizzas include:')
for pizza in friend_pizzas:
    print(pizza)