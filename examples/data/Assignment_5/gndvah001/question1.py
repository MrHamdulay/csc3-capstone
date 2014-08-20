"""UCT BBS
Vahin Gounden
16 April 2014"""

#defaults
msg = "no message yet"
file_1 = "42.txt"
file_2 = "1015.txt"

while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

#get input from user
    sel = input("Enter your selection:\n")

#if user selects enter message function
    if sel == "E" or sel == "e":
        msg = input("Enter the message:\n")
    elif sel == "V" or sel == "v":
        print("The message is:",msg)
    elif sel == "L" or sel == "l":
        print("List of files:"," ",file_1,","," ",file_2,sep = "")
    elif sel == "D" or sel == "d":
        name = input("Enter the filename:\n")
        if name == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif name == "1015.txt":
            print("Computer Science class notes ... simplified","Do all work","Pass course","Be happy",sep = "\n")
        else:
            print("File not found")
    elif sel == "X" or sel == "x":
        print("Goodbye!")
        break
    
    
    
