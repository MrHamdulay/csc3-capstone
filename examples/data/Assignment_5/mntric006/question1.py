newmessage = "no message yet" 
notexit = True            

def mainmenu():     
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")             
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
  
while notexit == True:          
    mainmenu()
    selection = input("Enter your selection:\n")    
    if selection.upper() == "X":
        print("Goodbye!")               
        notexit=False
        
    elif selection.upper() == "E": 
        newmessage = input("Enter the message:\n")  
        
    elif selection.upper() == "V":             
        print("The message is: " + newmessage)
        
    elif selection.upper() == "L":                   
        print("List of files: 42.txt, 1015.txt")
        
    elif selection.upper() == "D":
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