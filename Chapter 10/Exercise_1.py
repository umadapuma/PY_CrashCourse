#10-1 Learning Python:
# Print after reading in whole file
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

##print by looping over the file object
filename = 'learning_python.txt'
print('\n')
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n")
#print by storing lines in a list
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print('\nCheck\n')
#10-2 Learning C:
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.replace('Python','C').strip())
