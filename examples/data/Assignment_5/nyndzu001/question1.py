"""Dzunisani Nyoni
15 April 2014
A program to view prompts"""

filenames= "42.txt, 1015.txt"

def welcome():
    """Prints a welcome message"""
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

msg=""

def list():
    print("List of files:", filenames)
    
def display():
    filename=input("Enter the filename:\n")
    if filename=="42.txt":
        print("The meaning of life is blah blah blah ...")
    elif filename=="1015.txt":
        print("Computer Science class notes ... simplified")
        print("Do all work")
        print("Pass course")
        print("Be happy")
    else:
        print("File not found")


welcome()
selection=input("Enter your selection:\n").lower()
#msg=""

while selection != "x":
   # welcome()
    
    if selection=="e":
        msg=input("Enter the message:\n")
    
    elif selection=="v":
        if msg=="":
            print("The message is: no message yet")
        else:
            print("The message is:",msg)
        
    elif selection=="l":
        list()
    elif selection=="d":
        display()

    welcome()
    selection=input("Enter your selection:\n")
else:
    print("Goodbye!")
    
    #selection=input("Enter your selection:\n").lower()
    
    
    
#    elif selection
    