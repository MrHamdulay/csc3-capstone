
message='no message yet'
while(10>0):
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    sel=input('Enter your selection:\n')
    if sel=='E' or sel=='e':
        message=input('Enter the message:\n')
        continue
        if sel=='V' or sel=='v':
            print('The message is:', message)
    elif sel=='V'or sel=='v':
        print('The message is:', message)
    elif sel=='L' or sel=='l':
        print('List of files: 42.txt, 1015.txt')
        continue
    elif sel=='D' or sel=='d':
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
    elif sel=='X' or sel=='x':
        print('Goodbye!')
        break