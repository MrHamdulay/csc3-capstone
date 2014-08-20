#Assignment 5, Question 1, Program to display messages and files
#LYLON002
#15 April 2014

newmessage = "no message yet"  #default message
keeprunning = True                  #boolean variable for loop

def mainmenu():     
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")             #displays the main menu
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
  
while keeprunning == True:          #loop to run program
    mainmenu()
    selection = input("Enter your selection:\n")    #get selection
    if selection.upper() == "X":
        print("Goodbye!")               #exit is called, loop ends
        keeprunning=False
        
    elif selection.upper() == "E": 
        newmessage = input("Enter the message:\n")  #entering the message
        
    elif selection.upper() == "V":              #show message
        print("The message is: " + newmessage)
        
    elif selection.upper() == "L":                      #list of filenames
        print("List of files: 42.txt, 1015.txt")
        
    elif selection.upper() == "D":
        filename = input("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename == "1015.txt":                                    #view contents of files
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")