c = ' '
msg = ''
file42txt = 'The meaning of life is blah blah blah ...'
file1015txt = '''Computer Science class notes ... simplified
Do all work
Pass course
Be happy'''

while c!='x':
    print('''Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it''')
    
    c = input('Enter your selection:\n').lower()
    
    if c=='e':
        # enter a message
        msg = input('Enter the message:\n')
    elif c=='v':
        print('The message is: ',end='')
        if msg!='': print(msg)
        else: print('no message yet')
    elif c=='l':
        print('List of files: 42.txt, 1015.txt')
    elif c=='d':
        fn = input('Enter the filename:\n')
        if fn=='42.txt':
            print(file42txt)
        elif fn=='1015.txt':
            print(file1015txt)
        else:
            print('File not found')
    elif c=='x':
        print('Goodbye!')