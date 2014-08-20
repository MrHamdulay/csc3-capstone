def BBS():
    #print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:')
   # x = input()
    mess = ''
    x = ''
    while x != 'X' or x != 'x':
        print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:')
        x = input()
        if x == 'E' or x == 'e':
            mess = input('Enter the message:\n')
        elif x == 'V' or x == 'v':
            if not mess:
                print('The message is: no message yet')
            else:
                print('The message is:',mess)
        elif x == 'L' or x == 'l':
            LIST = print('List of files: 42.txt, 1015.txt')
        elif x == 'D' or x == 'd':
            DISPLAY = input('Enter the filename:\n')
            if DISPLAY == '1015.txt':
                print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
            elif DISPLAY == '42.txt':
                print('The meaning of life is blah blah blah ...')
            else:
                print('File not found')
                
        elif x == 'X' or x == 'x':
            print('Goodbye!')
            break

BBS()