#Basic meny
#Thea Sitek, STKTHE002
#14.04.21014

selection = 'I'
message = ''

#Print options
while selection != 'X':
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')

    selection = input('Enter your selection: \n')
    selection = selection.upper()

    if selection == 'E':
        message = input('Enter the message: \n')
    
    elif selection == 'V':
        if message:
            print('The message is:', message)
        else:
            print('The message is: no message yet')
    
    elif selection == 'L':
        files = print('List of files: 42.txt, 1015.txt')
    
    elif selection == 'D':
        display = input('Enter the filename: \n')
        if display == '42.txt':
            print('The meaning of life is blah blah blah ...')
        elif display == '1015.txt':
            print('Computer Science class notes ... simplified')
            print('Do all work')
            print('Pass course')
            print('Be happy')
        else:
            print('File not found')
   
    elif selection == 'X':
        print('Goodbye!')
    
    
    


