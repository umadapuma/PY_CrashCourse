#10-6 Addition:
#10-7 Addition Calculator:
while('number3' not in locals()):
    try:
        number1 = int(input("first number?"))
        number2 =int( input("second number?"))
        number3 = number1 + number2
    except ValueError:
        print("Brother in Crist, when I ask for numbers please enter a number.")
    else:
        print(number3)

#10-8 Cats and Dogs:
#10-9 Silent Cats and Dogs:
def read_files(filename):
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.split()
        for word in words:
            print(word)
    print('\n')

filename = 'cats.txt'
read_files(filename)
filename = 'checkfile.txt'
read_files(filename)
filename = 'dogs.txt'
read_files(filename)

#10-10 Common Words:
def word_amount(filename):
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        temp = contents.lower().count('the')

    print(f"The word 'the' is in {filename} " + str(temp)+" times.")

filenames = ['Franken.txt','GrimmsFT.txt','RnJ.txt']
for filename in filenames:
    word_amount(filename)