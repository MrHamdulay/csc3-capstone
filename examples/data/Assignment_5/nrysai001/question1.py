





a="yes"
while a.upper() != "X" :
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    a=input("Enter your selection:\n")
    if a.upper() == "E":
        b=input("Enter the message: \n")
        
        
    elif a.upper() == "V" :
        try:
            print("The message is:",b)
            
        except NameError:
            print("The message is: no message yet")
            
        
    elif a.upper() == "D":
        c=input("Enter the filename:\n")
        try:
            opend= open ( c, 'r' )
            opend=opend.read()
            print(opend)
            
        except IOError:
            print("File not found")
            
    elif a.upper() == "L":
        print("List of files: 42.txt, 1015.txt")
        
        
print("Goodbye!")
        
        
    

