# question1.py
# jono field
# 16 april 2014
# program to simulate a simple BBS with one stored message and two fixed files

p="The meaning of life is blah blah blah ..."
a="Computer Science class notes ... simplified"
b="Do all work"
c="Pass course"
d="Be happy"
selection="E"

while selection!="x": # create loop to run program until user exits
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection=input("Enter your selection:\n")
    if selection=="v": # if user chooses "v" before entering a message
            print("The message is: no message yet")    
    if selection=="e": # if user selects "e"
        message=input("Enter the message:\n") # get message
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection=input("Enter your selection:\n")
        if selection=="v": # if selection is "v" when "e" exists
            print("The message is:",message) # print last message entered
    if selection=="l": # if user selects "l"
        print("List of files: 42.txt, 1015.txt") # list files
    if selection=="d": # if user selects "d"
        filename=input("Enter the filename:\n") # user enters file name
        if filename=="42.txt":
            print(p)
        elif filename=="1015.txt":
            print(a)
            print(b)
            print(c)
            print(d)
        else:print("File not found") # if file does not exist
print("Goodbye!") # if user selects "x", program ends
