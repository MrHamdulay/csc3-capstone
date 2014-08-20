"""mymath
alexander whiting
18 april 2014"""

message = "no message yet"
option =0
while option != "X":
    print("Welcome to UCT BBS")
    print("MENU\n\
(E)nter a message\n\
(V)iew message\n\
(L)ist files\n\
(D)isplay file\n\
e(X)it\
    ")
    option = input("Enter your selection:\n").upper()
    if option == 'E':
        message = input("Enter the message:\n")
    elif option == "V":
        print("The message is: "+message)
    elif option == "L":
        print("List of files: 42.txt, 1015.txt")
    elif option == 'D':
        file = input("Enter the filename:\n")
        if file == '42.txt':
            print("The meaning of life is blah blah blah ...")
        elif file == '1015.txt':
            print("Computer Science class notes ... simplified\n\
Do all work\n\
Pass course\n\
Be happy")
        else:
            print("File not found")
    elif option == "X":
        print("Goodbye!")