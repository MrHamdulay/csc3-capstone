#Ikhlaas Pohplonker
#15 April 2014
#a program that simulates a simple BBS with one stored message and 2 fixed files
p="The meaning of life is blah blah blah ..."
a="Computer Science class notes ... simplified"
b="Do all work"
c="Pass course"
d="Be happy"
selection="E"
#keeps asking a user to enter a selection until user enters x
while selection!="x":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection=input("Enter your selection:\n")
    if selection=="v":
            print("The message is: no message yet")    
    if selection=="e":
        message=input("Enter the message:\n")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection=input("Enter your selection:\n")
        if selection=="v":
            print("The message is:",message)
    if selection=="l":
        print("List of files: 42.txt, 1015.txt")
    if selection=="d":
        filename=input("Enter the filename:\n")
        if filename=="42.txt":
            print(p)
        elif filename=="1015.txt":
            print(a)
            print(b)
            print(c)
            print(d)
        else:print("File not found")
print("Goodbye!")
            
        
    
    