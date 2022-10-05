#8-16 Imports:
"""import one_function
album_dict = one_function.make_album('lady gaga','olala')
print(album_dict)"""

"""from one_function import make_album
album_dict = make_album('lady gaga','olala')
print(album_dict)"""

"""from one_function import make_album as ma
album_dict = ma('lady gaga','olala')
print(album_dict)"""

"""import one_function as one
album_dict = one.make_album('lady gaga','olala')
print(album_dict)"""

from one_function import *
album_dict = make_album('lady gaga','olala')
print(album_dict)