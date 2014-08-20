__author__ = 'George de Kock'
#2014-04-13
message = "no message yet"
while True: #Continue asking for input until the user inputs X to exits
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    selection = input("Enter your selection:\n").upper()
    if selection == "E":
        message = input("Enter the message:\n")
    elif selection == "V":
        print("The message is:",message)
    elif selection == "L":
        print("List of files: 42.txt, 1015.txt")
    elif selection == "D":
        filename = input("Enter the filename:\n")
        if filename in"42.txt 1015.txt":
            textfile = open(filename)
            print(textfile.read())
        else:
            print("File not found")
    elif selection == "X":
        print("Goodbye!")
        break