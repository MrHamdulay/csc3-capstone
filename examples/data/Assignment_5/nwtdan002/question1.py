"""Simulation of a BBS Server
By Daniel Newton
13/04/14"""

def menu():     #The text displayed as the menu for the program.
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

mes="no message yet"    #The default message

while menu:     #Determining whether the program should still be run, which is the case until menu=False, when user enters X to exit.
    menu()
    ans=input("Enter your selection:\n")    #Prompts user to enter their choice from menu printed above.
    if ans=="X" or ans=="x":    #Cause the program to exit
        menu=False
        print("Goodbye!")
        
    elif ans=="E" or ans=="e":  #Asks the user to enter a new message, changing the previous or default one.
        mes=input("Enter the message:\n")
        
    elif ans=="V" or ans=="v":  #Displays messgae
        print("The message is:",mes)
        
    elif ans=="L" or ans=="l":  #Lists the 2 fixed files
        print("List of files: 42.txt, 1015.txt")
        
    elif ans=="D" or ans=="d":  #Prompts the user to enter a fixed file name to view its description.
        file=input("Enter the filename:\n")
        if file=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")