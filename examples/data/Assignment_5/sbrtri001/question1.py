# Assignment 5, question 1
# Tristan Subroyen
# 13 April 2014

def welcomeMessage(): # This function simply prints welcome message
    print("Welcome to UCT BBS")

def menu(): # This function prints the program menu
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
def main(): # This function performs the main processes of the program
    i = 0 # initialize i to 0 for while loop
    message = "no message yet" # default message
    files = ['42.txt','1015.txt'] # initialize array files
    while i == 0: # while loop
        welcomeMessage() # displays menu and welcome message
        menu()
        sel = input("Enter your selection:\n").upper()
        if sel == 'X':
            print("Goodbye!")
            i = i + 1 # causes loop to terminate
        elif sel == 'E':
            message = input("Enter the message:\n")
            i = i + 0
        elif sel == 'V':
            print("The message is:",message)
            i = i + 0
        elif sel == 'L':
            print("List of files: " + files[0] + ", " + files[1])
            i = i + 0
        elif sel == 'D':
            file = input("Enter the filename:\n")
            if file == '42.txt':
                print("The meaning of life is blah blah blah ...")
                i = i + 0
            elif file == '1015.txt':
                print("Computer Science class notes ... simplified"+"\n"+"Do all work"+"\n"+"Pass course"+"\n"+"Be happy")
                i = i + 0
            else:
                print("File not found")
                i = i + 0
                                    
if __name__ == '__main__':
    main()
    
    
        
            
            
    
            
        
        