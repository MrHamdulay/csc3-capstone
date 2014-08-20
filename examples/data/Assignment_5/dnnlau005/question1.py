"""a simple BBS with 1 stored message and 2 fixed files
Lauren Denny
14 April 2014"""

message = "no message yet"
s=""

#display menu
while s!="X": #keeps asking for a selection until selection is X(quits program) 
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")

#ask for a selection
    s = input("Enter your selection:\n")
    s = s.upper()

#performs action according to selection
    if s=="E":
        message = input("Enter the message:\n")
    elif s=="V":
        print("The message is:", message)
    elif s=="L":
        print("List of files: 42.txt, 1015.txt")
    elif s=="D":
        filename = input("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    elif s=="X":
        print("Goodbye!")
        