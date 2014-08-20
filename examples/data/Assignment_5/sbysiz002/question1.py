x=''
y=''
File1 ='Computer Science class notes ... simplified\n'+'Do all work\n'+'Pass course\n'+'Be happy' 
File2= 'The meaning of life is blah blah blah ...'
while x != 'X':
    M= 'Welcome to UCT BBS\n'
    M+= 'MENU\n'
    M+= '(E)nter a message\n'
    M+= '(V)iew message\n'
    M+= '(L)ist files\n'
    M+= '(D)isplay file\n'
    M+= 'e(X)it'
    print(M)    
    x=input('Enter your selection:\n')
    x=x.upper()
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