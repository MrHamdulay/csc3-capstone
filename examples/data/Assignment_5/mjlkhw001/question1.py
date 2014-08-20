# UCT BBS
# Khwezi Majola
# MJLKHW001
# 14 April 2014

def bbs():
    letter = ''
    mes = 'no message yet'
    while letter != 'x':
        letter = input('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n',)
        letter = letter.lower()
        if letter == 'e':
            mes = input('Enter the message:\n', )
        elif letter == 'v':
            print('The message is:', mes)
        elif letter == 'l':
            print('List of files: 42.txt, 1015.txt')
        elif letter == 'd':
            filename = input('Enter the filename:\n')
            if filename == '42.txt':
                print('The meaning of life is blah blah blah ...')
            elif filename == '1015.txt':
                print('Computer Science class notes ... simplified', 'Do all work', 'Pass course', 'Be happy', sep = '\n')
            else: print('File not found')
    print('Goodbye!')
bbs()