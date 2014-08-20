#Assignment 5
#Question 1

import os
selection = 0
message="no message yet"

while selection != "X":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection=input("Enter your selection:\n").upper()
    if selection == "E":
        message=input("Enter the message:\n")
        print(message)
    if selection == "V":
        print("The message is:"," ",message," ",sep="")
    if selection == "L":
        listfiles=os.listdir()
        print("List of files:"," ",listfiles[0],", ",listfiles[1],sep="")
        
    if selection == "D":
        filesel=input("Enter the filename:\n")
        file=open(filesel,'r')
        print(file.read())
               
print("Goodbye!")


