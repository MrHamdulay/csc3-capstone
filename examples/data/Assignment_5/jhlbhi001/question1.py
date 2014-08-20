entered_selection=""
entered_message="no message yet" 
while(entered_selection!="X" and entered_selection!="x"):
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

    entered_selection=input("Enter your selection:\n")
    
    if entered_selection=="E" or entered_selection=="e":
        entered_message=input("Enter the message:\n")
           
   
    elif entered_selection=="V" or entered_selection=="v":
        print("The message is:",entered_message)
       
        
    elif entered_selection=="L" or entered_selection=="l":
        print("List of files: 42.txt, 1015.txt")
                
    elif entered_selection=="D" or entered_selection=="d":
        entered_filename= input("Enter the filename:\n")
        if entered_filename=="42.txt":
            print("The meaning of life is blah blah blah ...")
                                             
        elif entered_filename=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
           
        else:
            print("File not found")
                                       
                                   

print("Goodbye!")       