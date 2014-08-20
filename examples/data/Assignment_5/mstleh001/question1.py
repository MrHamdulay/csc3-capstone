#Lehlgonolo Masetla

x=''
y=''
File1 ='Computer Science class notes ... simplified\n'+'Do all work\n'+'Pass course\n'+'Be happy' 

File2= 'The meaning of life is blah blah blah ...'

while x != 'X': #ensures menu repeat unless an exit is selected
    
    # menu options
    
    sentence= 'Welcome to UCT BBS\n'
    sentence+= 'MENU\n'
    sentence+= '(E)nter a message\n'
    sentence+= '(V)iew message\n'
    sentence+= '(L)ist files\n'
    sentence+= '(D)isplay file\n'
    sentence+= 'e(X)it'
    
    print(sentence)   
    
    x=input('Enter your selection:\n')
    x=x.upper() # ensures input is in upper case
    
    if x == 'E':
        y=input('Enter the message:\n')
    elif x == 'V':
        if y == '':
            print('The message is: no message yet')
        else:    
            print('The message is:',y)
    elif x == 'D':
        F=input('Enter the filename:\n')
        if F == '1015.txt':
            print(File1)
        elif F == '42.txt':
            print(File2)
        else:
            print('File not found')
    elif x == 'L':
        print('List of files: 42.txt, 1015.txt')
print('Goodbye!')            