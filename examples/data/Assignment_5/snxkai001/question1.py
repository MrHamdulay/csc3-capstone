#kairav soni
msg=1

enter=""


while enter!=("X") and enter!=("x"):
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    enter=input("Enter your selection:\n")
    
    

    if enter==("E") or enter==("e"):
        msg=input("Enter the message:\n")
        
        
    if enter==("V") or enter==("v"):
            
        if msg!=(1):
            print("The message is:" ,msg)
            
            
            
        if msg==(1):
            print("The message is: no message yet")
            
            
        
    if enter==("l") or enter==("L"):
        print("List of files: 42.txt, 1015.txt")
        
        
        
    if enter==("d") or enter==("D"):
        enter1=input("Enter the filename:\n")
        
        
        
        if enter1==("42.txt"):
            print("The meaning of life is blah blah blah ...")
            
            
            
        if enter1==("1015.txt"):
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            
            
            
        if enter1!=("42.txt") and enter1!=("1015.txt"):
            print("File not found")
            
            
            
    if enter==("X") or enter==("x"):
        print("Goodbye!")
    
    