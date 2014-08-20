"""BBS Simulator
Geoff Murphy
MRPGEO001
13 April 2014"""

message = ""

def BBS():
    global message    #Allows 'message' to be used both inside and outside the function
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selec = input("Enter your selection:\n")
    
    #runs certain if statement depending on input
    if selec == "e" or selec == "E":
        message = str(input("Enter the message:\n")) #stores the entered message
        BBS()                                        #invokes the function continuously
        
    elif selec == "v" or selec == "V":
        if message == "":
            print("The message is: no message yet") #Displays if no message was entered
            BBS()
        else:
            print("The message is:",message)        #Displays the stored message
            BBS()    
    
    elif selec == "x" or selec == "X":              #Exits the function, i.e. it does not invoke it again
        print("Goodbye!")
          
    elif selec == "d" or selec == "D":
        file = input("Enter the filename:\n")
        if file == "1015.txt":                      #Nested if's run depending on the input of the filename
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            BBS()
        elif file == "42.txt":
            print("The meaning of life is blah blah blah ...")
            BBS()
        else:
            print("File not found")                  #Displays if invalid file name is entered
            BBS()
            
    elif selec == "l" or "L":
        print("List of files: 42.txt, 1015.txt")      #Displays the list of files
        BBS()
    
    
BBS()