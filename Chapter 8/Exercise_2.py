#8-6 City Names:
def city_country(city,country):
    return (city.title()+", "+country.title())
cc = city_country('santiago','chile')
print(cc)
print(city_country('london','england'))
print(city_country('tokyo','japan'))

#8-7 Album:
def make_album(artist,title):
     album = {'artist':artist,'album':title}
     return album
album_dict = make_album('Bobbi',"Supermusic")
print(album_dict)
album_dict = make_album('Deriik','Silent music')
print(album_dict)
album_dict = make_album('lady gaga','olala')
print(album_dict)

#8-8 User Albums:
def make_album(artist,title):
     album = {'artist':artist,'album':title}
     return album
     
while True:
    print('\nPlease tell me who is the artist and their album')
    print("enter 'q' to quit")

    artist = input('Artist: ')
    if artist == 'q':
        break
    album = input('Album: ')
    if album == 'q':
        break


    album_dict = make_album(artist,album)
    print(album_dict)
