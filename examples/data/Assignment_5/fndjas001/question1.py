"""A program that simulates a Bulletin Board System
Jason Findlay
14/04/2014"""

choice=""
message=""

while choice!="X" and choice!="x":
    choice=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")

    if choice=="E" or choice=="e":
        message=input("Enter the message:\n")
    elif choice=="V" or choice=="v":
        if message=="":
            print("The message is: no message yet")
        else:
            print("The message is:",message)
    elif choice=="L" or choice=="l":
        print("List of files: 42.txt, 1015.txt")
    elif choice=="D" or choice=="d":
        filename=input("Enter the filename:\n")
        if filename=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
print("Goodbye!")
