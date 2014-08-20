#UCT BBS PROGRAM
#Lauren de Bruyn
#16 April 2014

Choice=""
defaultmessage=False
#Display menu until user exits
while Choice!= "X":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice=input("Enter your selection: \n")
    Choice= choice.upper()
    if Choice=="L":
        print("List of files: 42.txt, 1015.txt")
    elif Choice=="D":
        file=input("Enter the filename: \n")
        if file=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    elif Choice=="E":
        message=input("Enter the message:\n")
        defaultmessage= True
    elif Choice=="V":
        if defaultmessage==True:
            print("The message is:",message)
        else:
            print("The message is: no message yet")
    elif Choice== "X":
        print("Goodbye!")


