#4-3 Counting to Twenty:
for value in range(1,21):
    print(value)

#4-4
million = list(range(1,1000001))
#for value in million:
#    print(value)

#4-5
print(min(million))
print(max(million))
print(sum(million))

#4-6

odds = list(range(1,21,2))
for odd in odds:
    print(odd)

#4-7
threes = list(range(3,31,3))

for three in threes:
    print(three)
print('----------------------------------')
#4-8
cubes=[]
for number in range(1,11):
    cubes.append(number**3)

for number in cubes:
    print(number)

#4-9
squares = [number**3 for number in range(1,11)]

print(squares)
print('------------------------------------')
#4-10 Slices
print('The first three items listed are:')
print(squares[:3])

print('\nThree items from the middle include:')
print(squares[4:7])

print('\nThe last three items are:')
print(squares[7:])
