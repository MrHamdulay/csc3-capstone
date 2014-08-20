"""Simple  Bulletin Board Systems (BBS)
Sbongakonke Mlangeni
14 April 2014"""
logic = True
def xy():
    logic = True
    a = ''
    while logic == True:
        count = 0
        a = ''
        print('Welcome to UCT BBS')
        print('MENU')
        print('(E)nter a message')
        print('(V)iew message')
        print('(L)ist files')
        print('(D)isplay file')
        print('e(X)it')
        x = input('Enter your selection:\n')
        x = x.upper()
        if x == 'E':
            msg = input('Enter the message:\n')
            count += 1
        elif count == 0:
            print('No message yet')
            
            
        elif x == 'V' and count == 1:
            print('The message is:',msg)
        elif count == 0:
            print('Message not found yet')
        
        elif x == 'X':
            print('Goodbye!')
            logic = False
        elif x == 'L':
            files = ['42.txt','1015.txt']
            print('List of files:',files[0:])
        elif x == 'D':
            file = input('Enter the file name:\n')
            files = ['42.txt','1015.txt']
            
            if file == '42.txt':
                print('The meaning of life is blah blah blah')
            if file == '1015.txt':
                print('Computer Science class notes ... simplified')
                print('Do all work')
                print('Pass course')
                print('Be happy')
            else:
                print('File not found')
    
            
            
xy()