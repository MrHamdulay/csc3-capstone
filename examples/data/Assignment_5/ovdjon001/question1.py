""" Assignment 5 Questiosn 1 by Jonathan Ovadia
on the 16 April 2014"""
global m 
m = "no message yet"
def menu():
    print("Welcome to UCT BBS \nMENU \n(E)nter a message\n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")
    c = input("Enter your selection: \n")
    return c
def enter():
    global m
    m = input("Enter the message:\n")
def view():
    print("The message is:",m)
def list_files():
    print("List of files: 42.txt, 1015.txt")
def display():
    filename = input("Enter the filename:\n")
    if filename == "42.txt":
        print("The meaning of life is blah blah blah ...")
    elif filename== "1015.txt":
        print("Computer Science class notes ... simplified","Do all work","Pass course","Be happy", sep = "\n")
    else:
        print("File not found")
        
    
def main():
    c = menu().lower()
    while c != "x":
        if c == "e":
            enter()
            c = menu()
        elif c == "v":
            view()
            c = menu()
        elif c == "l":
            list_files()
            c = menu()
        elif c == "d":
            display()
            c = menu()
    else:
        print("Goodbye!")        
main()