def txt():
    print("The meaning of life is blah blah blah ...")
def other_txt():
    print("Computer Science class notes ... simplified")
    print("Do all work")
    print("Pass course")
    print("Be happy")
    
def Mr_main():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    #store a file
    mr_file=("")
    
    #get selection
    select=input("Enter your selection:\n")
    
    #output for E
    while select!="x" and select!="x":
        
        if select=="E" or select=="e":
            x=input("Enter the message:\n")
            mr_file+=x
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")

            
            select=input("Enter your selection:\n")  
            
    #output for V
        elif select=="V" or select=="v":
            if mr_file==(""):
                print("The message is: no message yet")
            else:
                print("The message is:",mr_file)
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")            
            
            select=input("Enter your selection:\n")  
    #ouput for L
    
        elif select=="L" or select=="l":
            print("List of files: 42.txt, 1015.txt")
            print("Welcome to UCT BBS")
            
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")            
                        
            select=input("Enter your selection:\n")  
    #output for D
        elif select=="D" or select=="d":
            file=input("Enter the filename:\n")
            if file==("42.txt"):
                x=txt()
                print("Welcome to UCT BBS")
                
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")            
                
                select=input("Enter your selection:\n")                  
        
            elif file==("1015.txt"):
                x=other_txt()
                print("Welcome to UCT BBS")

                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")            
                
                select=input("Enter your selection:\n")  
            else:
                print("File not found")
                print("Welcome to UCT BBS")
                
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")            
                
                select=input("Enter your selection:\n")                  
        #exit
    if select=="x":
        print("Goodbye!")
Mr_main()
        
        
        