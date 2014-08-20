#Nikhil Jiten Naik
#Comsci 1015F
#Assignment 5

def mainMethod():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    message = ""
    selection =input("Enter your selection: \n")
    while selection!="x":
    
        if selection == "e":
            message = input("Enter the message: \n")
          
        elif selection == "v":
            if message == "":
                print("The message is: no message yet")
            else:
                print("The message is: "+message)
           
        elif selection == "l":
            print("List of files: 42.txt, 1015.txt")
            
        elif selection == "d":
            fileName = input("Enter the filename: \n")
            if fileName == "42.txt":
                print("The meaning of life is blah blah blah ...")
                
            elif fileName == "1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
               
            else:
                print("File not found")
       
        elif selection == "x":
            print("Goodbye!")        
        
        print("Welcome to UCT BBS")        
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection =input("Enter your selection: \n") 
        
    if selection == "x":
            print("Goodbye!")
    

            
            
        
        
        
mainMethod()