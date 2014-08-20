selection = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")

message=""

while(selection != "X" or selection != "x"): 

    if (selection =="E" or selection == "e"):
        message = input("Enter the message:\n")

    elif (selection == "V" or selection == "v"):

        if (message == ""):
            print("The message is: no message yet")
        else:
            print("The message is: "+message)

    elif (selection == "L" or selection == "l"):
        print("List of files: 42.txt, 1015.txt")

    elif (selection == "D" or selection == "d"):
        file=input("Enter the filename:\n")

        if(file=="42.txt"):
            print("The meaning of life is blah blah blah ...")

        elif(file=="1015.txt"):
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")

        else:
            print("File not found")

    elif(selection=="x" or selection=="X"):
        break

    selection = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
print("Goodbye!")