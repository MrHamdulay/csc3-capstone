"""Simulation of a simple Bulletin Board System"""
#Brandon Pickup
#2014/04/14
#Assignment 5 Question 1

file = open("42.txt","w")
file.write("The meaning of life is blah blah blah ...")
file.close()

file = open("1015.txt","w")
file.write("Computer Science class notes ... simplified\n")
file.write("Do all work\n")
file.write("Pass course\n")
file.write("Be happy")
file.close()

fileList=["42.txt","1015.txt"]
def displayMenu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
def main():
    message="no message yet"
    displayMenu()
    userInput = input("Enter your selection:\n")
    if userInput.upper() == "X":
        print ("Goodbye!")    
    while (userInput.upper() != "X"):
        if userInput.upper() == "E":
            message = input("Enter the message:\n")
        elif userInput.upper() == "V":
            print ("The message is:",message)
        elif userInput.upper() == "X":
            print ("Goodbye!")        
        elif userInput == "l":
            print("List of files: ", ", ".join(fileList),sep="")
        elif userInput.upper() == "D":
            try:
                fileName = input("Enter the filename:\n")
                file = open(fileName,"r")
                content = file.read()
                print(content)
            except IOError:
                print("File not found")
        displayMenu()
        userInput = input("Enter your selection:\n")
        if userInput.upper() == "X":
            print ("Goodbye!")        
main()