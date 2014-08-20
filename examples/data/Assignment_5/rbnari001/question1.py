#Ariel Rubin
#RBNARI001
#16 April 2014
# a program to create a BBS system for UCT

#creating variables with blank strings (will be used later in program)
message = ""
selection = ""

#while loop to display menu for BBS system
#menu will continue to display until user enters x
while selection.upper() != "X":
    print ("Welcome to UCT BBS")
    print ("MENU")
    print ("(E)nter a message")
    print ("(V)iew message")
    print ("(L)ist files")
    print ("(D)isplay file")
    print ("e(X)it")
#ask user to enter a selection    
    selection = input ("Enter your selection:\n")
#if user enters e, user is able to enter a message    
    if selection.upper() == "E":
        message = input("Enter the message:\n")
#if user enters v, user is able to view a message
# if there is no message then the user is prompted with "no message yet"
#if there is a message then the message will be displayed 
    if selection.upper() == "V":
        if message == "":
            print ("The message is: no message yet")
        else:
            print ("The message is:",message)
#if user enters x, the while loops ends and program displays goodbye 
    if selection.upper() == "X":
        print ("Goodbye!")
#if user enters l, user is view the list of files         
    if selection.upper() == "L":
        print ("List of files: 42.txt, 1015.txt")
#if user enters d, user is asked to enter a name of a file
#if user enters a file with the name 1015.txt, information is displayed from that file
#if user enters a file with the name 42.txt, information is displayed from that file
#if user enters a file that does not exist, the user is notified that the file cant be found
    if selection.upper() == "D":
        filename = input ("Enter the filename:\n")
        if filename == "1015.txt":
            print ("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print ("Be happy")
        elif filename == "42.txt":
            print ("The meaning of life is blah blah blah ...")
        else:
            print ("File not found")