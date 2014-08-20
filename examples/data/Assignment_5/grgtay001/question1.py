"""bulletin board system
tayla george
16 april 2014"""




message ="no message yet"#one stored message


    
def menu():
    message ="no message yet"
    while True:
        print('Welcome to UCT BBS')
        print('MENU')
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection = input("Enter your selection:\n")
        if selection =='e' or selection =='E':
            message= input("Enter the message:\n")
        
        elif selection =='V' or selection== 'v':
            print("The message is:",message,end='\n')
            
        elif selection =='L' or selection=='l':
            print("List of files: 42.txt, 1015.txt")
        
        elif selection =='D' or selection=='d':
            filename = input("Enter the filename:\n")
            if filename== "42.txt": #fixed file
                print("The meaning of life is blah blah blah ...")
                
            elif filename =="1015.txt": #fixed file
                print("Computer Science class notes ... simplified",end='\n')
                print("Do all work",end='\n')
                print("Pass course",end='\n')
                print("Be happy",end='\n')
            
            else:
                print("File not found")            
            
        elif selection =='X' or selection=='x':
            print("Goodbye!")
            break 
menu()
    
    
    
    
    
    
  
        
        

        
        