#Code to choose Options
#Saul Bloch
#14 April 2014

messages = "no message yet"

def intro():
    #prints out welcome message
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    
    
    selection = input("Enter your selection:\n")
    
    if (selection == "E" or selection == "e"):
        global messages #allows the variable to be used elsewhere
        messages = input("Enter the message:\n") #prompts user for message
        intro()
    
    elif (selection == "V" or selection == "v"):
        print("The message is: "+ messages) #prints user message
        intro()
    
    elif (selection == "L" or selection == "l"):
        print("List of files: 42.txt, 1015.txt") #lists files
        intro()
    
    elif (selection == "D" or selection == "d"):
        file = input("Enter the filename:\n") #prompts user for file name
        #prints out file of user's choice
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else: print("File not found")
        intro()
    elif (selection == "X" or selection == "x"):
        print("Goodbye!")    

intro()
