"""Bulletin Board System
Kumaran Reddy
16 April 2014"""

Answer="0"
message="no message yet"
#'X' AND 'x' mean exit,so loop should not run if that is selected
while Answer != 'X' or Answer != 'x':
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")    
    Answer=input("Enter your selection:\n")
    if Answer=='x' or Answer=='X':
        print("Goodbye!")
        break
    elif Answer=="e" or Answer=="E":
        message=input("Enter the message:\n")
    elif Answer=="v" or Answer=="V":
        print("The message is:",message)
    elif Answer=="l" or Answer=="L":
        print("List of files: 42.txt, 1015.txt")
    elif Answer=="d" or Answer=="D":
        file_name=input("Enter the filename:\n")
        if file_name== "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file_name== "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
            
            