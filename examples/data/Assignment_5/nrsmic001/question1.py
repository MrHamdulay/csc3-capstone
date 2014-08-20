""" Program to create BBS
Micaela Narasmulu
16 April 2014 """

selection=""
message="no message yet"

while selection != "X": #prints the menu and asks for a selection
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection=input("Enter your selection:\n")
    selection=selection.upper()
    
    if selection=="E":
            message=input("Enter the message:\n")
        
    elif selection=="V":
            print("The message is:",message)
        
    elif selection=="L":
            print("List of files: 42.txt, 1015.txt")
        
    elif selection=="D":
        filename=input("Enter the filename:\n")
        if filename=="42.txt":
                print("The meaning of life is blah blah blah ...")
        elif filename=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work\nPass course\nBe happy")
        else:
                print("File not found")    



print("Goodbye!")

    