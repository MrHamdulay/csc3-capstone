#Aaron Krishna 
#15 April 2014
#A program to simulate a simple BBS

message = "" #empty string that can be used to store a future message
selection = "" #empty string that can be used to store the users selection in menu

def menu(): #funtion displaying the menu
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
while selection != "X" or selection != "x":
    
    menu() #calls the menu funtion
    selection = input("Enter your selection:\n") #requests user to select a menu option
    
    if selection == "E" or selection == "e": #if user selected E or e
        message = input("Enter the message:\n") #requests user to enter a message
        
    if selection == "V" or selection == "v": #if user selected V or v
        if message == "": #if message is empty
            print("The message is: no message yet") #tells user that message is empty
        else:
            print("The message is:" , message) #if there is a message
            
    if selection == "L" or selection == "l": #if user selected L or l
        print("List of files: 42.txt, 1015.txt") #prints list of textfiles available
        
    if selection == "D" or selection == "d": #if user selected D or d
        filename = input("Enter the filename:\n") #requests user to enter the name of the file they want to display
        if filename == "42.txt": #if user selected file 42.txt
            print("The meaning of life is blah blah blah ...") #diplays file
        elif filename == "1015.txt": #if user selected file 1015.txt
            print("Computer Science class notes ... simplified", "Do all work","Pass course","Be happy", sep = "\n") #diplays file
        else: #if user selected a file that is not available
            print("File not found") #tells user that the file cannot be found
            
    if selection == "X" or selection == "x": #if user selected X or x
        print("Goodbye!") 
        break #ends program