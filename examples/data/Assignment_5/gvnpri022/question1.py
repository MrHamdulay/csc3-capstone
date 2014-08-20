"""question 1- assignment 5
prinesan govender
14 april 2014"""
choice=""
msg="" #initialise variables
while(choice!="X"):
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")    
    choice = (input("Enter your selection:\n")).upper() #converting to uppercase so that you dont have to check for both cases
    if (choice=="E"):
        msg= input("Enter the message:\n")

    elif(choice=="V"):
        if(msg==""):
            print("The message is: no message yet")
        else:
            print("The message is:",msg)
    
    elif(choice=="L"):
        print("List of files: 42.txt, 1015.txt")
    
    elif(choice=="D"):
        fName= input("Enter the filename:\n")
        if(fName=="42.txt"):
            print("The meaning of life is blah blah blah ...")
        elif(fName=="1015.txt"):
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")

print("Goodbye!") #message when loop has ended