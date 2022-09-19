#5-8 
#5-9
usernames = ['Bob','Bill','Jo','admin','Joanne','Jeff']
#usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello '+ user +' would you like to see a status report?')
        else:
            print('Hello ' + user + ', thank you for logging in again.')
else:
    print('There are no users')
print('------------------------------')

#5-10
current_users = ['bessyBot','getRECKd','TonyStarkcontrast','animeluver96','loadingscreeam']
lowered_current_users = [current_user.lower() for current_user in current_users]
new_users = ['bigtom','getreckd','frankstank','yUngdRip','PainSaga']

for user in new_users:
    if user.lower() in lowered_current_users:
        print('sorry youll need to use a different name')
    else:
        print('That user name works!')