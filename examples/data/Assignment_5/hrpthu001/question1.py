""" program to simulate a simple BBS
thushar hariparsad
15 april 2014"""

def print_():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
print_()
sel = input("Enter your selection:\n")
sel=sel.upper()
msg= "The message is: no message yet"
while sel!= "X":
    if sel=="":
        print(msg)
    if sel == "E":
        msg=input("Enter the message:\n")
        msg="The message is: "+msg
    if sel=="V":
        print(msg)
    if sel=="L":
        print("List of files: 42.txt, 1015.txt")
    if sel=="D":
        filename=input("Enter the filename:\n")
        if filename=="42.txt":
            print("The meaning of life is blah blah blah ...")
        if filename=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        if filename!= "42.txt" and filename!="1015.txt":
            print("File not found")
    
    print_()
    sel = input("Enter your selection:\n")
    sel=sel.upper()
print("Goodbye!")    