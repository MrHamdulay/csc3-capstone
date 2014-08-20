#Assignment 5:)
message =  "no message yet"
option = ''
while option != 'X':
    print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')
    option = input('Enter your selection:\n')
    option = option.upper()
    if option =='E':
        message = input('Enter the message:\n')
    elif option =='V':
        print('The message is:',message)
    elif option =='X':
        print('Goodbye!')
    elif option =='L':
        print('List of files: 42.txt, 1015.txt')
    elif option == 'D':
        fileName = input('Enter the filename:\n')
        if fileName =='42.txt':
            print('The meaning of life is blah blah blah ...')
        elif fileName==('1015.txt'):
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
        else:
            print('File not found')
    
        
        
    