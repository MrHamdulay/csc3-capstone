"""CSC1015F Assignment 5 Question 1
Xola Matlanyane MTLXOL002
17 April 2014"""

#creating the menu
def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

#creating the saved files
def txtfile1():
    print("The meaning of life is blah blah blah ...")
def txtfile2():
    print("Computer Science class notes ... simplified\n","Do all work\n","Pass course\n","Be happy",sep="")

#creating the selection
def select():
    E=""
    x=""
    while x.upper() != "X":
        menu()
        x=input("Enter your selection:\n")
        if x.upper() == "E":
            E=input("Enter the message:\n")
        elif x.upper() == "V":
            if E=="":
                print("The message is: no message yet")
            else:
                print("The message is:",E)
        elif x.upper() == "L":
            print("List of files: 42.txt, 1015.txt")
        elif x.upper() == "D":
            d=input("Enter the filename:\n")
            if d == "42.txt":
                txtfile1()
            elif d == "1015.txt":
                txtfile2()
            elif d != "42.txt":
                print("File not found")
            elif d != "1015.txt":
                print("File not found")
    print("Goodbye!")
    
select()