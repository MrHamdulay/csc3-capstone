'''Assignment 5 question 1 BBS program
Adam Smith
16 April 2014'''

def main(): #main method, contains the user selection part oft he program

    userInput = ""
    global message    
    message = ""
    
    while userInput.upper() != "X": #run program while user hasn't selected exit
        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        userInput = input("Enter your selection:\n")
        
        if userInput.upper() == "E":
            EnterMessage()
        elif userInput.upper() == "V":
            DisplayMessage()
        elif userInput.upper() == "L":
            ListFiles()
        elif userInput.upper() == "D":
            DisplayFile()
        elif userInput.upper() == "X":
            print("Goodbye!")

def EnterMessage(): #change the global variable message
    global message
    message = input("Enter the message:\n")
    
def DisplayMessage(): #output the global variable message
    if message == "":
        print("The message is: no message yet")
    else:
        print("The message is: " + message)
        
def ListFiles(): #list valid files
    print("List of files: 42.txt, 1015.txt")
    
def DisplayFile(): #display requested file or output error
    fileSelection = input("Enter the filename:\n")
    
    if fileSelection == "42.txt":
        print ("The meaning of life is blah blah blah ...")
    elif fileSelection == "1015.txt":
        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy") 
    else:
        print("File not found")

if __name__ == "__main__": #run the program
    main()