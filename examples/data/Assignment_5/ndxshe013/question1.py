
y = "no message yet"
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    
    x = input("Enter your selection:\n")
    if x.lower() == "e":
        y = input("Enter the message:\n")
        
    elif x.lower() == "v":
        print("The message is:",y)
        
    elif x.lower() == "x":
        print("Goodbye!")
        break
        
    elif x.lower() == "l":
        print("List of files: 42.txt, 1015.txt")
        
    elif x.lower() =="d":
        z = input("Enter the filename:\n")
        if z == "42.txt":
            print("The meaning of life is blah blah blah ...")
            
            
        elif z == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            
            
        else:
            print("File not found")


    

