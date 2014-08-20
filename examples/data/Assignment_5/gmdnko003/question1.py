#program depicting Bullitin Board System (BBS) used to exchange infromation
#nkosingiphile gumede
#16/04/2014

import time #for slight time lag to show file list & viewed message

i=1
c=1
while i!=0:
    #opening message
    print("Welcome to UCT BBS")
    print("MENU")
    #menu options
    print("(E)nter a message") #must save this message
    print("(V)iew message") #must show inputed message
    print("(L)ist files") #list consists of files: 42.txt and 1015.txt
    print("(D)isplay file") # shows message behind 1 of the 2 files
    print("e(X)it") #break and say Goodbye
    x=input("Enter your selection:\n")
    #print(str.upper(x)) used to convert all x to upper case
    #for E command
    if str.upper(x)=="E":
        c="1"
        y=input("Enter the message:\n") #variable y has stored message
    #for V command
    if str.upper(x)=="V":
        if c=="1":
            print("The message is:",y)
        else: print("The message is: no message yet")
    #for X command
    if str.upper(x)=="X":
        print("Goodbye!")
        i=0
    #for l command
    if str.upper(x)=="L":
        print("List of files: 42.txt, 1015.txt")
    #for d command
    if str.upper(x)=="D":
        z= input("Enter the filename:\n")
        if z=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif z=="1015.txt":
            print("Computer Science class notes ... simplified","Do all work","Pass course","Be happy",sep="\n")
        else:
            print("File not found")
          