#Kiuran Naidoo
#Assignment 5
#Question 1
message = "" #variable for message to return
choice = "" #Store user input
while choice != "X":
    print( "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    choice = input( "Enter your selection:\n").upper()   #input for choice

    #Do functions for various inputs
    if choice == "X":
        print("Goodbye!")
        break 
    if choice  == "V" and message == "":
        print( "The message is: no message yet")
    if choice == "V" and message != "":
        print( "The message is:", message)
    if choice == "E":
        message= input ("Enter the message:\n" )    
    if choice == "L":
        print ( "List of files: 42.txt, 1015.txt" )
    elif choice == "D":
        file = input ( "Enter the filename:\n" )
        if file == "42.txt":
            print ( "The meaning of life is blah blah blah ..." )
        elif file == "1015.txt":
            print ( "Computer Science class notes ... simplified" )
            print ( "Do all work" )
            print ( "Pass course" )
            print ( "Be happy" )
        else:
            print ( "File not found" )
            
