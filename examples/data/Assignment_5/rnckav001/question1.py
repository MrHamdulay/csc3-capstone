#ass.5 Q1    -   BBS
#Kavir Ranchod   -   RNCKAV001
#15/04/2014

msg="no message yet"
choice=""
while choice != "X" and choice != "x":
    choice=input(("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")).upper()
    if choice == "E" or choice == "e":    
        msg=input("Enter the message:\n")
    elif choice == "V" or choice == "v" :
        print("The message is:",msg)
    elif choice == "L" or choice == "l":
        print("List of files: 42.txt, 1015.txt")
    elif choice == "D" or choice == "d":
        filename=input("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        elif filename != "42.txt" and filename != "1015.txt":
            print("File not found")
    elif choice == "X":
        print("Goodbye!")
    else:
        continue