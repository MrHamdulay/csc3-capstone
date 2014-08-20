message='no message yet'
files=' 42.txt, 1015.txt'
file1='The meaning of life is blah blah blah ...'
file2a='Computer Science class notes ... simplified'
file2b='Do all work'
file2c='Pass course'
file2d='Be happy'
print ('Welcome to UCT BBS\n'+'MENU\n'+'(E)nter a message\n'+'(V)iew message\n'+'(L)ist files\n'+'(D)isplay file\n'+'e(X)it')
selection=input('Enter your selection:\n')
while selection=='e' or selection=='E' or selection=='v'or selection=='V' or selection=='l' or selection=='L' or selection=='d' or selection=='D' or selection=='X'or selection=='x':
    if selection=='e' or selection=='E':
        message=input('Enter the message:\n')
        print ('Welcome to UCT BBS\n'+'MENU\n'+'(E)nter a message\n'+'(V)iew message\n'+'(L)ist files\n'+'(D)isplay file\n'+'e(X)it')
        selection=input('Enter your selection:\n')
    if selection=='v' or selection=='V':
        print('The message is:',message)
        print ('Welcome to UCT BBS\n'+'MENU\n'+'(E)nter a message\n'+'(V)iew message\n'+'(L)ist files\n'+'(D)isplay file\n'+'e(X)it')
        selection=input('Enter your selection:\n')
    if selection=='l' or selection=='L':
        print('List of files:'+files)
        print ('Welcome to UCT BBS\n'+'MENU\n'+'(E)nter a message\n'+'(V)iew message\n'+'(L)ist files\n'+'(D)isplay file\n'+'e(X)it')
        selection=input('Enter your selection:\n')            
    if selection=='d' or selection=='D':
        filename=input('Enter the filename:\n')
        if filename=='42.txt':
            print(file1)
            print ('Welcome to UCT BBS\n'+'MENU\n'+'(E)nter a message\n'+'(V)iew message\n'+'(L)ist files\n'+'(D)isplay file\n'+'e(X)it')
            selection=input('Enter your selection:\n')
        elif filename=='1015.txt':
            print(file2a,file2b,file2c,file2d,sep='\n')
            print ('Welcome to UCT BBS\n'+'MENU\n'+'(E)nter a message\n'+'(V)iew message\n'+'(L)ist files\n'+'(D)isplay file\n'+'e(X)it')
            selection=input('Enter your selection:\n')        
        else:
            print('File not found')
            print ('Welcome to UCT BBS\n'+'MENU\n'+'(E)nter a message\n'+'(V)iew message\n'+'(L)ist files\n'+'(D)isplay file\n'+'e(X)it')
            selection=input('Enter your selection:\n')        
    if selection=='X'or selection=='x':
        print('Goodbye!')
        break