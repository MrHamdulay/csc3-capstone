"""PROGRAM TO DISPLAY MENU AND OPTIONS
DIVAN JAGERS
JGRDIV001
15 APRIL 2014"""
b="no message yet" # IF V IS AN EMPTY STRING
while True: #DISPLAYS MENU
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    a=input("Enter your selection:\n")
    a=a.lower()
                                # ALL THE IF AND ELIF STATEMENTS LINKS TO WHAT THE USER INPUTS
    if a== "e":
        b=input("Enter the message:\n") #STORES A NEW VALUE FOR B
    elif a =="v":
        print("The message is:",b) 
    elif a == "l":
        print("List of files: 42.txt, 1015.txt")
    elif a == "d":
        c=input("Enter the filename:\n")
        if c == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif c == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        elif c != "42.txt"or "1015.txt":
            print("File not found")
    elif a == "x":                     #SENTINEL
        print("Goodbye!")
        break

    