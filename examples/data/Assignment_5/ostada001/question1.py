#Adam Oosthuizen
#mymath
#17 April 2014
'''UCT Bulletin Board System'''
#Declaration of variables
default = "no message yet"
fileError = "File not found"

data = ""
file  = open("42.txt","r")
file2 = open("1015.txt","r")

#While loop that runs until x is entered. This will print out the menu and its functions
while data !="X":
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    data = input("Enter your selection:\n").upper()
    
    if data == "X":
        print("Goodbye!")
        break
    elif data == "E":
        default = input("Enter the message:\n")
    elif data == "V":
        print("The message is: "+ default)
    elif data == "L":
        print("List of files: 42.txt, 1015.txt")
    elif data == "D":
        filename = input("Enter the filename:\n")
        if filename == "42.txt":
            print (file.read())
        elif filename == "1015.txt":
            print (file2.read())
        else:
            print("File not found")
        
        
        