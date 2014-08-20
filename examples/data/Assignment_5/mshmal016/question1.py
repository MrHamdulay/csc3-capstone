
b=""
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

    a=input("Enter your selection:\n")
    a=a.lower()
    if a=="e":
        b=input("Enter the message:\n")
        continue
        
    elif a=="v":
        if b=="":
            print("The message is: no message yet")
        else:    
            print("The message is:",b)
    #else:
        #print("no message yet")
          
    elif a=="x":
        print("Goodbye!")
        break
    
    elif a=="l":
        print("List of files: 42.txt, 1015.txt")
        
    elif a=="d":
        c=input("Enter the filename:\n")
        if c=="42.txt":
            print("The meaning of life is blah blah blah ...")
            
        elif c=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            
        else:
            print("File not found")
        