"""Reece Gounden
Assignment 5 Q1
"""

wel = "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:"
sel =""
msg ="no message yet"
while sel != "X":
    print(wel)
    sel = input().upper()
    if sel=="E":
        msg = input("Enter the message:\n")
    if sel=="V":
        print("The message is: "+msg)
    if sel=="L":
        print("List of files: 42.txt, 1015.txt")
    if sel=="D":
        x = input("Enter the filename:\n")
        if x == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif x == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
print("Goodbye!")