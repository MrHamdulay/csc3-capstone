# uct bbs program
# tarisai kalinde
# klntar002

def uctbbs():
    #initialising j and k for while loop to run
    j=' '
    k=''
    #while loop for the bringing back of the print statement m
    while j!='x':
        
        m=print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')        
        j=input('Enter your selection:\n')
        #selections
        if j=='E' or j=='e':
            k=input('Enter the message:\n')
                    
        elif j=='V' or j=='v':
            if k=='':
                print('The message is: no message yet')
            else:
                print('The message is:',k)
                
        elif j=='l' or j=='L':
            print('List of files: 42.txt, 1015.txt')
            
        elif j=='d' or j=='D':
            y=input('Enter the filename:\n')
            if y=='42.txt':
                print('The meaning of life is blah blah blah ...')
            elif y=='1015.txt':
                print('Computer Science class notes ... simplified')
                print('Do all work')
                print('Pass course')
                print('Be happy')
            else:
                if y!='42.txt' or y!='1015.txt':
                    print('File not found')
                
        if j=='x' or j=='X':
            print('Goodbye!')
            break # so that program ends when 'x' is prompted
        
        
        
uctbbs()    