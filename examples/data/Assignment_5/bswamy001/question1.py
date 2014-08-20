""""Amy Bosworth, Assignment 5, question 2, program to produce a simple BBS"""



select= 'X', 'E', 'V', 'L', 'D', 'x', 'e', 'v', 'l', 'd' #Users options


msg="no message yet" 

#keep iterating until exit
while select!= 'X' or 'x':
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    select=input("Enter your selection:\n")
    
    if select=='V' or select=='v':
        print("The message is:",msg)
        
    elif select=='E' or select=='e':
        msg=input("Enter the message:\n")
        
    elif select=='L' or select=='l':
        print("List of files: 42.txt, 1015.txt")
        
    elif select=='D' or select=='d':
        file=input("Enter the filename:\n")
        if file== '42.txt':
            print("The meaning of life is blah blah blah ...")
        elif file=='1015.txt':
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
            
    elif select=='X' or select=='x':
        print("Goodbye!")
        break
   
    
         





        
    
    