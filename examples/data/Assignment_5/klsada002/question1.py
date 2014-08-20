#Programme to simulate BBS
#Adam Kaliski
#CSC1015 Assignment 5

choice = ''
message = 'no message yet'
while choice != 'X':
    choice = input(('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n')).upper()
    if choice == 'E':
        message = input('Enter the message:\n')
    elif choice == 'V':
        print('The message is:',message)
    elif choice == 'L':
        print('List of files: 42.txt, 1015.txt')
    elif choice == 'D':
        c=input('Enter the filename:\n')
        if c == '42.txt':
            print('The meaning of life is blah blah blah ...')
        elif c == '1015.txt':
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
        else:
            print('File not found')
    elif choice == 'X':
        print('Goodbye!')