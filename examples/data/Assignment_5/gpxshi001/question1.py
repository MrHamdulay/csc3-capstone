#GPXSHI001
#17th April
#Q1

import glob


message = 'no message yet'
print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")

sel = input("Enter your selection:\n")

while True:
    
    if sel in 'Ee':
        message = input('Enter the message:\n')
        
    elif sel in 'Xx':
        break
    
    elif sel in 'Vv':
        print('The message is:', message)
        
    elif sel in 'Ll':
        print('List of files:', ', '.join(glob.glob('*.txt')[::-1]))
        
    elif sel in 'Dd':
        myfile = input('Enter the filename:\n')
        
        if myfile not in glob.glob('*.txt'):
            print('File not found')
            
        else:
            myfile = open(myfile, 'r')
            
            for i in myfile:
                print(i, end = '')

    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    sel = input("Enter your selection:\n")    
    
print('Goodbye!')