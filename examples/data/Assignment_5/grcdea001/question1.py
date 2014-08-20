"""Program to mimic basic bulitin board system, prac 5 question 1 
Dean Gracey
4/15/2014"""


choice = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
message = "no message yet"
import os

while (choice!="X") or (choice!="x"):#only runs while choice is not an x 
    if(choice == "E") or (choice == "e"):
        message=input("Enter the message:\n")
        choice = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
        
    if (choice == "V") or (choice=="v"):
        print("The message is:", message, sep = " ")
        choice = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
        
    if (choice == "L") or (choice=="l"):
        files = os.listdir()
        files.reverse()
        top  = "List of files: "
        for i in files:
            if ".txt" in i:
                top = top + i + ", "
        top = top[:len(top)-2]
        print(top)
        choice = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
        
    if (choice == "D") or (choice=="d"):
        name = input("Enter the filename:\n")
        
        try:
            f = open(name)
            filec = f.read()
            print(filec)
            choice = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
        except :
            print("File not found")
            choice = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    if (choice == "X") or (choice=="x"):
        print("Goodbye!")    
        break # ensures does not get stuck in endless loop
        
