#6-7 People
bob = {'first_name':'Bob',
        'last_name':'Barker',
        'age': 13000, 
        'city':'Planet Namek'}

thomas = {'first_name':'Thomas',
        'last_name':'Terry',
        'age': 20, 
        'city':'Colorado'}
sharen ={'first_name':'Sharen',
        'last_name':'Pierce',
        'age': 45, 
        'city':'San Francisco'}
people =[bob,thomas,sharen]

for person in people:
    print (person)
print('-------------------------------------------')
#6-8 Favorite Numbers
rex = {'type':'dog',
        'owner': 'Bill',
        }
birdy = {'type':'bird',
            'owner':'Laura'}
bilbo = {'type':'cat',
            'owner':'Derek'}
pets = [rex,birdy,bilbo]


print('-------------------------------------------')

#6-9 Favorite Places
favorite_places = {'missy':['paris','detroit'],
                    'melanie':['north dakota'],
                    'delany':['california','mississippi','florida']}
for name,places in favorite_places.items():
    print('\n'+name.title() + "'s favorite places include:")
    for place in places:
        print("\t"+ place.title())

#6-10 Favorite Numbers:


names = {'Bill':[69,234,234],'Tom':[1,3,420],'Teri':[9,13],'Kevin':[42],
            'Derek':[555,849,218,6743]}
for person,numbers in names.items():
    print('\n'+ person + "'s favorite numbers include")
    for number in numbers:
        print('\t'+ str(number))

#6-11 cities
cities = {'manhattan':{
            'country':'usa',
            'population':'10000000',
            'fact':'statue liberty here'
            },
            'seattle':{
                'country':'usa',
                'population':'5000000',
                'fact':'location of needle'
            },
            'seoul':{
                'country':'south korea',
                'population':'11000000',
                'fact': 'offical name seoul special city'
            }
}
for city, city_info in cities.items():
    print("\ncity: " + city.title())
    country = city_info['country'].title()
    population = city_info['population'].title()
    fact = city_info['fact']
    print('\tCountry: ' + country)
    print('\tPopulation: ' + population)
    print('\tFact: '+ fact )

