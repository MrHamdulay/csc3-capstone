"""Lungelo Mdunge.
Assignment 5, question 1"""

print("Welcome to UCT BBS","\n","MENU",sep="")
print("(E)nter a message","\n","(V)iew message","\n","(L)ist files","\n","(D)isplay file","\n","e(X)it",sep="")
enter=input("Enter your selection:\n")
L="List of files: 42.txt, 1015.txt"
input_=enter.upper()
x="Goodbye!"
m="no message yet"

while input_!= "X": #Create a constraint through a loop
    if input_== "E":
        message=input("Enter the message:\n")
        m=message
    elif input_== "V":
        print("The message is:",m)
    elif input_== "L":
        print(L)
    elif input_=="D":
        files=input("Enter the filename:\n")
        if files=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif files=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    print("Welcome to UCT BBS","\n","MENU",sep="")
    print("(E)nter a message","\n","(V)iew message","\n","(L)ist files","\n","(D)isplay file","\n","e(X)it",sep="")
    enter=input("Enter your selection:\n")
    input_=enter.upper()
print(x)
        
        
        
        
