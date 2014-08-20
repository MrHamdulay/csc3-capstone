#Riya Desai
#Assignment 5
#16 April 2014

import glob

#Print the list of commands
message = 'no message yet'
print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")

#Ask user for an input
selection = input("Enter your selection:\n")

while True:
    if selection in 'Ee':
        message = input('Enter the message:\n')
    elif selection in 'Xx':
        break
    elif selection in 'Vv':
        print('The message is:', message)
    elif selection in 'Ll':
        print('List of files:', ', '.join(glob.glob('*.txt')[::-1]))
    elif selection in 'Dd':
        myfile = input('Enter the filename:\n')
        if myfile not in glob.glob('*.txt'):
            print('File not found')
        else:
            myfile = open(myfile, 'r')
            for i in myfile:
                print(i, end = '')
#Print commands     
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection = input("Enter your selection:\n")    
    
print('Goodbye!')