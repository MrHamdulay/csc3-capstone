""" A program to simulate a simple BBS with one stored message and 2 fixed files, as indicated in the output
Author: Afika Nyati
Date: 15th April 2014"""

current_message = "no message yet" # I have created this global variable so that the default message can be 'no message yet'.


def enter_message():
    
    global current_message   # The 'global' signifies that the 'current_message' is the global variable, no one created in this function.
    
    current_message = input("Enter the message:\n")



def view_message():
    
    print("The message is:", current_message) # Prints the global current_message.
        
    

def list_files():
    
    print("List of files: 42.txt, 1015.txt")
    


def display_file():
    
    filename = input("Enter the filename:\n")
    
    if filename == "42.txt":
        print("The meaning of life is blah blah blah ...")
    elif filename == "1015.txt":
        print("Computer Science class notes ... simplified")
        print("Do all work\n", "Pass course\n", "Be happy", sep = "")
        
    else:
        print("File not found")
    
    

def main():
    
    while True:
        
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
    
        selection = str.lower(input("Enter your selection:\n"))
    
    
        if selection == "e":
            enter_message()
    
    
    
        if selection == "v":
            view_message()
    
    
    
        if selection == "l":
            list_files()
    
    
    
        if selection == "d":
            display_file()
    
    
    
        if selection == "x":
        
            print("Goodbye!")
            break
        
    
    
if __name__ == "__main__":
    
    main()