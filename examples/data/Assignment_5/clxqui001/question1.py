"""this program allows users in a community to exchange information
quincy cele
14 april 2014"""
file= True

while file== True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice=input("Enter your selection:\n")
    if choice=="e" or choice== "E":
        message=input("Enter the message:\n")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        choice=input("Enter your selection:\n")
        if choice=="v" or choice=="V":
            print("The message is:",message)
    elif choice == "v" or choice=="V":
        print("The message is: no message yet")
    elif choice== "l" or choice=="L":
        print("List of files: 42.txt, 1015.txt")
    elif choice == "d" or choice=="D":
        file_chosen=input("Enter the filename:\n")
        if file_chosen== "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file_chosen== "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        elif choice!="42.txt" and "1015.txt":
            print("File not found")
    elif choice== "x" or choice=="X":
            print("Goodbye!")
            break
        
        
            
        
        

        
        
        
        
        
        
    
        
            
    
    
    