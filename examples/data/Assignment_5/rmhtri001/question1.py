z= ""
y= ""
while z != "X":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    answer = input("Enter your selection:\n")
    answer = answer.upper()
    
    
    if answer == "E":
        y = input("Enter the message:\n")
    
    elif answer == "V":
        
        if y == "":        
            print ("The message is: no message yet")       
        else:
            print("The message is:", y)
      
    elif answer == "L":
        print("List of files: 42.txt, 1015.txt")
    
    elif answer == "D":
        filename = input("Enter the filename:\n")
        
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        
        else:
            print("File not found")
        
    elif answer == "X":
        print("Goodbye!")
   
    z = answer