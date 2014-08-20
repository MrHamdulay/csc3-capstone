"""Program to simulate a simple BBS.
Kemeshan Naicker
16 April 2014"""

def UCT_BBS():
#Open files.
    file1 = open("42.txt", "r")
    file2 = open("1015.txt", "r")
#Set default message.
    message = "no message yet"
#Get BBS to run until user opts to exit.    
    while "live":
#Print menu interface.
        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        choice = input("Enter your selection:\n").lower()
        if choice == "e":
#Get and store message from user.
            message = input("Enter the message: \n")
        elif choice == "v":
            if message:
                print("The message is:", message, sep=" ")
#List files.
        elif choice == "l":
            print("List of files: 42.txt, 1015.txt")
#Display a selected file.
        elif choice == "d":
            chosenfile = input("Enter the filename: \n")
            if chosenfile == "42.txt":
                print(file1.read())
            elif chosenfile == "1015.txt":
                print(file2.read())
            else:
                print("File not found")
#Terminate when user inputs "x".
        elif choice == "x":
            print("Goodbye!")
            break

UCT_BBS()
            
        
