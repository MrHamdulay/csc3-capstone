"""A Program to simulate a BBS with built in files
By Jeremy Smith SMTJER002
14 April 2014"""

import os
#set initial message
message= "no message yet"

#print a bbs selection menu
selection=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")

#loop a bbs selection menu until user exits
while selection != "X" and selection != "x":
    if selection == "E" or selection == "e":
        message=input("Enter the message:\n")
        selection=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    elif selection == "V" or selection == "v":
            print("The message is:", message)
            selection=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    elif selection == "L" or selection == "l":
        files=[]
        for file in os.listdir():
            if file.endswith(".txt"):
                files.append(file)
                files.reverse()
                allfiles = ", ".join(files)
        print("List of files:", allfiles)            
        selection=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    elif selection == "D" or selection == "d":
        fname=input("Enter the filename:\n")
        if fname not in os.listdir():
            print("File not found")
            selection=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
        else:
            infile=open(fname,"r")
            data = infile.read()
            print(data)        
            selection=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
                
print("Goodbye!")

