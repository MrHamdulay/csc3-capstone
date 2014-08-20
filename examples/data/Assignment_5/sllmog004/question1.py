"""Assignment 5 question 1
Yaseen Sulliman
16 April 2014"""

message="no message yet"
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    
    selection=input("Enter your selection:\n")
    selection = selection.upper()

    if selection=="E":
        message=input("Enter the message:\n")
    elif selection=="V":
        print("The message is:", message)
    elif selection=="L":
        print("List of files: 42.txt, 1015.txt")
    elif selection=="D" or selection=="d":
        file=input("Enter the filename:\n")
        if file=="42.txt":
            txt42=open("42.txt","r")
            print(txt42.read())
        elif file=="1015.txt":
            txt1015=open("1015.txt","r")
            print(txt1015.read())
        else:
            print("File not found")
    elif selection=="X":
        print("Goodbye!")
        break
     
        