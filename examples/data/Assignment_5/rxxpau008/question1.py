#Description: Simple Bulletin Board System
#Name: Paul Roux - RXXPAU008
#Date: 15 April 2014

import glob

def menu(): #Used to generate the menu
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice = input("Enter your selection:\n")
    return choice

x = menu()
message = "no message yet"

while x: #Runs until the user enters an 'X'
    x = x.upper()
    if x == "E":#Gets a message
        message = input("Enter the message:\n")
        x = menu()
    elif x== "V":#Displays the stored message
        print("The message is:",message)
        x = menu()
    elif x == "L":#Lists the files 
        print("List of files: ",end='')
        out = ''
        for i in glob.glob("*.txt"):#Used to get the file names of any .txt files in the folder
            out = i+', '+out
        print(out[:len(out)-2])
        x = menu()
    elif x == "D":#Displays the files
        try: #Used in case the user enters a filename that doesn't exist
            name = input("Enter the filename:\n")
            f = open(name)
            print (f.read())
        except:
            print("File not found")
        x = menu()
    elif x == "X":#Ends the loop and the program
        print("Goodbye!")
        x = False