"""program for simulating a basic BBS
casey o'donnell
15 april 2014"""

message="no message yet"
file1="The meaning of life is blah blah blah ..."
file2="Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"

while True:
        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        inp=input("Enter your selection:\n")
        if inp == "E" or inp=="e":
                message=input("Enter the message:\n")
        if inp=="V" or inp=="v":
                print("The message is:",message)
        if inp=="L" or inp=="l":
                print("List of files: 42.txt, 1015.txt")
        if inp=="D" or inp=="d":
                inpD=input("Enter the filename:\n")
                if inpD=="42.txt":
                        print(file1)
                elif inpD=="1015.txt":
                        print(file2)
                else:
                        print("File not found")
        if inp=="X" or inp=="x":
                print("Goodbye!")
                break