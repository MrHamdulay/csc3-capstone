# Assignment 5 question 1
# Amy Brodie
# 16/04/2014

selection = ""

# the welcome messages and menu
def welcome():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
message = "no message yet"

# get user input and give appropriate output
while True:
    welcome()
    selection = input("Enter your selection:\n")
    if selection.upper() == "E":
        message = input("Enter the message:\n")
    elif selection.upper() == "V":
        print("The message is:",message)
    elif selection.upper() == "L":
        print("List of files: 42.txt, 1015.txt")
    elif selection.upper() == "D":
        file_name = input("Enter the filename:\n")
        if (file_name == "42.txt") or (file_name == "1015.txt"):
            file_contents = open(file_name)
            contents = file_contents.read()
            file_contents.close
            print(contents)
        else:
            print("File not found")
    elif selection.upper() == "X":
        print("Goodbye!")
        break