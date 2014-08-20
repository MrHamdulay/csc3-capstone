"""Question 1 of Assignment 5: BBS
Shaheel Kooverjee
17th April 2014"""

decision = " "
message = "no message yet"

while decision: #display options
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    decision = input("Enter your selection:\n")
    
    if decision == "e" or decision == "E": #enter message
        message = input("Enter the message: \n")
    if decision == "v" or decision == "V": #display message
        print("The message is:", message)
    if decision == "l" or decision == "L": #list files
        print("List of files: 42.txt, 1015.txt")
    if decision == "d" or decision == "D": #display file
        file = input("Enter the filename: \n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        elif file != "42.txt" or file != "1015.txt":
            print("File not found")
    if decision == "x" or decision == "X": #exit
        print("Goodbye!")
        break
    