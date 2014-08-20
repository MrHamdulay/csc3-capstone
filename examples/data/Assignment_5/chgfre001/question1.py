#a simple BBS service program
#by frederick chigwaza
#15 april 2014

def bbs_service():
    
#initialising variables    
    choice=' '
    msg=' '
    
    while choice!='x':
        menu=print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')
       
    
        choice=input('Enter your selection:\n')
        
        if choice=='e'or choice=='E':
            msg=input('Enter the message:\n')
        elif choice=='v'or choice=='V':
            if msg==' ':
                print('The message is: no message yet')
            else:
                print('The message is:',msg)
                
        elif choice=='L' or choice=='l':
            print('List of files: 42.txt, 1015.txt')
        
        elif choice=='d' or choice=='D':
            filename=input('Enter the filename:\n')
            if filename=='1015.txt':
                print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
            elif filename=='42.txt':
                print('The meaning of life is blah blah blah ...')
            else:
                if filename!='42.txt' or filename!='1015.txt':
                    print('File not found')
        if choice=='x'or choice=='X':
            print('Goodbye!')
            
            break
   
       
            
            
bbs_service()        
        
    
            
        
            
            
            
            


               
            
    