#10-3 Guest:
flag = True
"""
name = input("What's your name?")
filename ='guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(name)

#10-4 Guest Book:
filename = 'guest_book.txt'
with open(filename, 'w') as file_object:    
    while(flag == True):
        temp = input('Would you like to continue? y/n')
        if temp != 'y':
            break
        name = input("What's your name?")
        print('Nice to meet you ' + name)
        file_object.write(name + '\n')
"""
#10-5 Programming Poll:
filename = 'reason.txt'
with open(filename, 'w') as file_object:    
    while(flag == True):
        
        reason = input('Why do you like programming?')
        file_object.write(reason + '\n')
        
        temp = input('Would you like to continue? y/n')
        if temp != 'y':
            break