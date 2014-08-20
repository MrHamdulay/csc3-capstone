"""Assignment 5
functions and flow of control mechanisms
Chris Bolton"""

#Intro and Menu
def menu():
    print( "Welcome to UCT BBS")
    print( "MENU")
    print( "(E)nter a message" )
    print( "(V)iew message" )
    print( "(L)ist files" )
    print( "(D)isplay file" )
    print( "e(X)it" )
    

selection = 0
message = "no message yet"
while selection != "X":
    menu()
    selection = input( "Enter your selection:\n")   
    selection = selection.upper()
    
    if selection  == "V":
        print ("The message is:" , message )
    #if selection == "V":
       # print( "The message is:", message)
    if selection == "E":
        message= input ("Enter the message:\n" )    
    if selection == "X":
        print("Goodbye!")
        break 
    if selection == "L":
        print ( "List of files: 42.txt, 1015.txt" )
    elif selection == "D":
        filename = input ( "Enter the filename:\n" )
        if filename == "42.txt":
            print ( "The meaning of life is blah blah blah ..." )
        elif filename == "1015.txt":
            print ( "Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy" )
            
        else:
            print ( "File not found" )