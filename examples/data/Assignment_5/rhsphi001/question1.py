'''  a program to simulate a simple BBS with one stored message and 2 fixed files, as indicated in the output
     Phillip Ruhesi
     16 April 2014'''
select=''
message='no message yet'
while select!='X' and select!='x':
        print('Welcome to UCT BBS')
        print('MENU')
        print('(E)nter a message')
        print('(V)iew message')
        print('(L)ist files')                               # Prints the menu 
        print('(D)isplay file')
        print('e(X)it')
        select=input('Enter your selection:\n')
        if select=='E' or select=='e':
                message=input('Enter the message:\n')         # prompts user to enter message
        elif select=='V' or select=='v':      
                print('The message is:',message)            # prints the stored message 
        elif select=='L' or select=='l':
                print('List of files: 42.txt, 1015.txt')    # prints the list of files available
        elif select=='D' or select=='d':
                file=input('Enter the filename:\n')           # prints contents of selected file
                if file=='42.txt':
                        print('The meaning of life is blah blah blah ...')
                elif file=='1015.txt':
                        print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
                else:
                        print('File not found')             # outputs message if file is not found
        elif select=='X' or select=='x':
                print('Goodbye!')                           # exits program
                