'''Joshen Credelio Jacob
16/04/14'''

message='no message yet'
while(1>0):
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    selection=input('Enter your selection:\n')
    if selection=='E' or selection=='e':
        message=input('Enter the message:\n')
        continue
        if selection=='V' or selection=='v':
            print('The message is:', message)
    elif selection=='V'or selection=='v':
        print('The message is:', message)
    elif selection=='L' or selection=='l':
        print('List of files: 42.txt, 1015.txt')
        continue
    elif selection=='D' or selection=='d':
        file=input('Enter the filename:\n')
        if file=='42.txt':
            print('The meaning of life is blah blah blah ...')
        elif file=='1015.txt':
            print('Computer Science class notes ... simplified')
            print('Do all work')
            print('Pass course')
            print('Be happy')
        else: 
            print('File not found')
        continue
    elif selection=='X' or selection=='x':
        print('Goodbye!')
        break