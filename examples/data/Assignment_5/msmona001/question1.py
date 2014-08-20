 
"""Printing for selections
Khanyisile Morudu
14 April 2014"""


# function which will print same thing each time it's called
def print_all():  
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

#first run of the function    
print_all()

#user to select option
selection  = input("Enter your selection:\n")

#this is the default message
message = "no message yet"
while selection.upper() != "X":
    if selection.upper() == "E":
        message = input("Enter the message:\n")
    if selection.upper() == "V":
        print("The message is: " + message)
    if selection.upper() == "L":
        print("List of files: 42.txt, 1015.txt")
    if selection.upper() == "D":
        file_name = input("Enter the filename:\n")
        if file_name == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file_name == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    print_all()
    selection  = input("Enter your selection:\n")
#if the selection is x, then nothing else needs to be printed
if selection.upper() == "X":
    print("Goodbye!")