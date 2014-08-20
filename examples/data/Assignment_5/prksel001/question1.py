"""UCT BBS
Limpho Parkies
17-04-2014"""

#variables
welcome=('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')
MENU=''
message="no message yet"

while MENU!='X' and MENU!='x':
    print(welcome)
    MENU=input('Enter your selection:\n')
    if MENU=='E' or MENU=='e':
        message=input('Enter the message:\n')
    elif MENU=='V' or MENU=='v':
        print('The message is:',message)
    elif MENU=='L' or MENU=='l':
        print('List of files: 42.txt, 1015.txt')
    elif MENU=='D' or MENU=='d':
        filname=input('Enter the filename:\n')
        if filname=='42.txt':
            print('The meaning of life is blah blah blah ...')
        elif filname=='1015.txt':
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
        else:
            print('File not found')
    if MENU=='X' or MENU=='x':
        print('Goodbye!')