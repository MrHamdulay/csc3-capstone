x=1
y=0
while x:
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    x=input('Enter your selection:\n')    
    if x=='e':
        y=input('Enter the message:\n')
    elif x=='v':
        if y!=0:
            print('The message is:',y)
        elif y==0:
            print('The message is: no message yet')
    elif x=='l':
        print('List of files: 42.txt, 1015.txt')
    elif x=='d':
        z=input('Enter the filename:\n')
        if z=='1015.txt':
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
        elif z=='42.txt':
            print('The meaning of life is blah blah blah ...')
        else:
            print('File not found')
    elif x=='x':
        print('Goodbye!')
        break
        