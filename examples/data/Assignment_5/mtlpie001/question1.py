"""PIET MOTALAOTA
17 APRIL 2014"""
def BBS():
    selection=''
    message_to_view=''
    while selection!='X':
        print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')
        
        option_select=input('Enter your selection:\n')
        """Asks the user to choose """
        option_uppercase=option_select.upper()
        
        if option_uppercase=='':
            print('The message is: no message yet')
        elif option_uppercase=='E':
            message=input('Enter the message:\n')
            message_to_view=message
        elif option_uppercase=='V':
            if message_to_view=='':
                print('The message is: no message yet')
            else:
                print('The message is:',message_to_view)
        elif option_uppercase=='X':
            print('Goodbye!')
        elif option_uppercase=='L':
            print('List of files: 42.txt, 1015.txt')
        elif option_uppercase=='D':
            file=input('Enter the filename:\n')
            if file=='42.txt':
                print('The meaning of life is blah blah blah ...')
            elif file=='1015.txt':
                print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
            else:
                print('File not found')
        else:
            print('File not found')
        selection=option_uppercase
BBS()
        