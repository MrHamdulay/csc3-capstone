"""Program that simulates a simple BBS
Mtunzi France
15 April 2014"""
def question1():
    answerz=""
    message=""
    while answerz != "X" and answerz != "x":
        #prints the menu
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        answer=input("Enter your selection:\n")#Asks the user to select an option
        if answer=="E" or answer=="e":
            message=input("Enter the message:\n")
        elif answer=="V" or answer=="v":
            if message=="":
                print("The message is: no message yet")
            else:
                print("The message is:",message)
        if answer=="L" or answer=="l":
            print("List of files: 42.txt, 1015.txt")
        if answer=="D" or answer=="d":
            file_name=input("Enter the filename:\n")
            if file_name=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            if file_name=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file_name != "1015.txt" and file_name != "42.txt":
                print("File not found")
        answerz=answer
    else:
        if answer=="X" or answer=="x":
            print("Goodbye!")
question1()