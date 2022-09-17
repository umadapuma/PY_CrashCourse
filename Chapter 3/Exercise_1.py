# 3-1 Names
names = ['Bob','Jim','Harry']

print(names[0], names[1], names[2])

# 3-2 Greetings
Bobmessage = f'{names[0].title()}, your an idiot.'
Jimmessage = f'{names[1].title()}, your an idiot.'
Harrymessage = f'{names[2].title()}, your an idiot.'
print(Bobmessage)
print(Jimmessage)
print(Harrymessage)

# 3-3 Your Own List
locamotion = ['bicycle', 'plane', 'horse']
bike = f'{locamotion[0].title()} is a fun way to travel'
ranking = f'Between traveling on {locamotion[0]}, {locamotion[1]}, and {locamotion[2]}, I would perfer {locamotion[1]}'
print(bike)
print(ranking)