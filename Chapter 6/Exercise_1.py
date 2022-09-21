#6-1 Person:
bob = {'first_name':'Bob',
        'last_name':'Barker',
        'age': 13000, 
        'city':'Planet Namek'}
print(bob)

#6-2 Favorite Numbers:
names = {'Bill':69,'Tom':420,'Teri':13,'Kevin':42,
            'Derek':555}
for peeps in names:
    print(peeps + f"'s favorite number is {names[peeps]}")
print('-------------------------------------------')
#6-3 Glossary
glossary = {'elif':'else-if','if':'check the value of statment',
                'else':'catchall statement','boolean':'true or false',
                'inequality':'determine whether two values are not equal'}

#6-4
for words in glossary:
    print(words + f': {glossary[words]}\n')
    
#6-5 Rivers
rivers ={'nile':'egypt',
            'amazon':'brazil',
            'ganges':'india'}

for x,y in rivers.items():
    print('The '+ x.title() + ' River runs through ' + y.title())
print('-------------------------------------------')

for river in rivers:
    print(river.title())
print('-------------------------------------------')
for city in rivers.values():
    print(city.title())

#6-6
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
should_take_poll = ['jen','tom','edward','dennis','rob']

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + '.')
print('--------------------------------------------')
for person in should_take_poll:
    if(person in favorite_languages.keys()):
        print(person.title() + ', THANKS for taking poll')
    else:
        print(person.title() + ', PLEASE take the poll')