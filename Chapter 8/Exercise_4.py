#8-12 Sandwiches:
from distutils.command.build import build


def sandwich_maker(*fillings):
    print('Your sandwich contains:')
    for filling in fillings:
        print(filling)
sandwich_maker('turkey','lettuce','tomatoes')
sandwich_maker('cheese')
sandwich_maker('ham','spam','lamb')

#8-13 User Profile:
def build_profile(first, last, **user_info):

    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
user_profile = build_profile('Bob','Barker',
                            hair_color = 'black',
                            field = 'compsci',
                            fav_color = 'red')
print(user_profile)

#8-14 Cars
def make_car(manufacture,model,**details):
    car={}
    car['manufacture'] = manufacture
    car['model'] = model
    for key, value in details.items():
        car[key] = value
    return car

car = make_car('subaru','outback',color='blue', tow_package=True)
print(car)