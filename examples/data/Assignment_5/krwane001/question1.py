print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")
msg=""
ans=input("Enter your selection:\n")

while ans == "e":
    msg=input("Enter the message:\n")
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    ans=input("Enter your selection:\n")
    
while ans == "v":
    if len(msg) > 0:
        print("The message is:",msg)
    else:
        print("The message is: no message yet")
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    ans=input("Enter your selection:\n")
    while ans == "e":
        msg=input("Enter the message:\n")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        ans=input("Enter your selection:\n")
        
while ans == ("l"):
    print("List of files: 42.txt, 1015.txt")
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    ans=input("Enter your selection:\n")
    while ans == "d":
        fn=input("Enter the filename:\n")
        if fn == "42.txt":
            print("The meaning of life is blah blah blah ...")
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")
            ans=input("Enter your selection:\n")            
        elif fn == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")            
            ans=input("Enter your selection:\n")            
        elif fn!="1015.txt" and fn!="42.txt":
            print("File not found")
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")
            ans=input("Enter your selection:\n")      
        
while ans == "d":
    fn=input("Enter the filename:\n")
    if fn == "42.txt":
        print("The meaning of life is blah blah blah ...")
    elif fn == "1015.txt":
        print("Computer Science class notes ... simplified")
        print("Do all work")
        print("Pass course")
        print("Be happy")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")        
    elif fn!="1015.txt" and fn!="42.txt":
        print("File not found")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        ans=input("Enter your selection:\n")    

 
    

while ans == "x":
    print("Goodbye!")
    break