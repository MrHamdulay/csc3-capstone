# Student Number: PRTNIC017
# Date: 4/13/14

message = 'no message yet'
files = ['42.txt', '1015.txt']
option = ''

while option != 'x':
    print('Welcome to UCT BBS', 'MENU', sep='\n')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    option = input('Enter your selection:\n')[0]
    option = option.lower()

    if option == 'e':
        message = input('Enter the message:\n')
    elif option == 'v':
        print('The message is:', message)
    elif option == 'l':
        print('List of files: ', end='')
        print(str(files)[1:-1].replace('\'', '', 4))
    elif option == 'd':
        file_name = input('Enter the filename:\n')
        if file_name in files:
            file = open(file_name, 'r')
            print(file.read(10000))
        else:
            print('File not found')
    elif option == 'x':
        print('Goodbye!')