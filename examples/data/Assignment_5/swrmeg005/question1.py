#A program to simulate a simple BBS with one stored message and 2 fixed files
#Megan Swartz
#16 April 2014

#make an introductory message that can be repeated
def intro_message():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

#make a function to run the BBS
def BBS():
    intro_message()
    stored_message = ""   #allows us to accomodate for when there is no message yet
    selection = input("Enter your selection:\n")
    
    #analyse selection and run accordingly 
    while selection.upper() != "X": #if user enters X, we want to break
        
        if selection.upper() == "E":
            message = input("Enter the message:\n")
            stored_message += message
            
        if selection.upper() == "V":
            if stored_message == "":
                print("The message is: no message yet")
            else:
                print("The message is:",stored_message)
                
        if selection.upper() == "L":
            print("List of files: 42.txt, 1015.txt")
            
        if selection.upper() == "D":
            name_file = input("Enter the filename:\n")
            
            if name_file == "42.txt":
                print("The meaning of life is blah blah blah ...")
                
            elif name_file == "1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
                
            else:
                print("File not found")    
        intro_message()
        selection = input("Enter your selection:\n")
    print("Goodbye!")  
     
                
BBS()