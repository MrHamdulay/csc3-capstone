#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     13-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

message = ""

while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection = input("Enter your selection: \n").upper()
    if selection == "E":
        message = input("Enter the message: \n")
    elif selection == "V":
        if message:
            print("The message is:", message)
        else:
            print("The message is:", "no message yet")
    elif selection == "L":
        print("List of files: 42.txt, 1015.txt")
    elif selection == "D":
        name = input("Enter the filename: \n")
        if name == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif name == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    elif selection == "X":
        print("Goodbye!")
        break
