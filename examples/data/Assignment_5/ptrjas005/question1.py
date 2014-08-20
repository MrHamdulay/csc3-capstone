'''Jason Pietersen'''
def Message():
    print("Welcome to UCT BBS\nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it \n")
    x=input('Enter your selection: \n')
    while x not in "Xx":
        
        #selection
        if x in'Ee':
            y= input('Enter the message: \n')
             
        
        #selection
        elif (x=='V') or (x=='v'):
            print("The message is:",y)
            
        
        #selection
        elif (x=='X') or (x=='x'):
            print('Goodbye!')
            d
        #selection
        elif (x=='l') or (x=='L'):
            print("List of files: 42.txt,1015.txt")
            
            
        if (x=='d') or (x=='D'):
            display= input("Enter the filename:\n")
            if (display== '42.txt'):
                print("The meaning of life is blah blah blah ...")
                
            elif (display== '1015.txt'):
                print('Computer Science class notes ... simplified \n'+'Do all work \n'+'Pass course'+'Be happy')
                
            else:
                print("File not found")

                
        print("Welcome to UCT BBS\nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \nD)isplay file \ne(X)it \n")
        x=input('Enter your selection: \n')            
        
        
            
        
Message()