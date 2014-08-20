"""Recreate old BBS system
Ross Eyre
16/04/2014"""



#set user choice, msg and files
c = ""
msg = "no message yet"
files = ""

#Loop through menu until user enters 'X' to exit
while (c != "X"):
    print("Welcome to UCT BBS")
    c = input("MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n").upper()
    
    #perform different functions depending on user input
    if c == "E":
        msg = input("Enter the message:\n")
    elif c == "V":
        print("The message is: " + msg)
    elif c == "L":
        print("List of files: 42.txt, 1015.txt")        
    elif c == "D":
        fileN = input("Enter the filename:\n")
        if fileN == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif fileN == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")            
        else:
            print("File not found")
    elif c == "X":
        print("Goodbye!")