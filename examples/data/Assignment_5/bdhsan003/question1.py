#BDHSAN003

x=True
msg='no message yet'

while(x==True):
    
    print("Welcome to UCT BBS \n","MENU\n","(E)nter a message\n","(V)iew message\n","(L)ist files\n","(D)isplay file\n","e(X)it",sep='')
    
    selection=input("Enter your selection:\n")
    
    if(selection=='X' or selection=='x'):
        
        print("Goodbye!") 
        x=False
    
    elif(selection=='E' or selection=='e'):
        
        msg=input("Enter the message: \n")
        
    
    elif(selection=='V' or selection=='v'):
        
        print("The message is:",msg)
    
    elif(selection=='l' or selection=='L'):
        
        list=print("List of files: 42.txt, 1015.txt")
    
    elif(selection=='d' or selection=='D'):
        
        file_n=input("Enter the filename:\n")
        
        if(file_n=='42.txt'):
            
            print("The meaning of life is blah blah blah ...")
        
        elif(file_n=='1015.txt'):
            
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy",sep='')
            
        else:
            
            print("File not found")