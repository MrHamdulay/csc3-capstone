#simulating a simple BBS
#Kayla Hendricks
#16 April 2014

begin_choice = ""                      #starting as an empty string so that the loop condition will be true and it can begin.
message = ""                           #starting as an empty string so that "message" can be defined before hand even if user does not provide a message.
while begin_choice != "X" or "x":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice = input("Enter your selection:\n")
    if choice == "E" or choice == "e":
        view_message = input("Enter the message:\n")
        message+= view_message
    elif choice == "V" or choice == "v":
        if message !="":
            print("The message is:",message)
        else:
            print("The message is: no message yet")
    elif choice == "L" or choice == "l":
        print("List of files: 42.txt, 1015.txt")
    elif choice == "D" or choice == "d":
        file = input("Enter the filename:\n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    else:
        print("Goodbye!")
        break
    begin_choice+= choice             #concatenation of "begin_choice" and "choice" and making it equal "choice" so that, if loop did not break, it will run again.
    