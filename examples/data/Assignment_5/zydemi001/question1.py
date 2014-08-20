#A program to execute a BBS
#Author: Emiel Zyde
#Date: 17 April 2014


def intro():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
def main():
    intro()
    message = ""
    while True: 
       
        choice = input("Enter your selection:\n")
        if choice.lower() == "e":
            mess = input("Enter the message:\n")
            message+= mess
        elif choice.lower() == "v":
            if message == "":
                print("The message is: no message yet")
            else:
                print("The message is:",message)
        elif choice.lower() == "l":
            print("List of files: 42.txt, 1015.txt")
        elif choice.lower() == "d":
            file = input("Enter the filename:\n")
            if file == "42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file == "1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print("File not found")       
        elif choice.lower() == "x": 
            print("Goodbye!")
            break 
        intro()
    
    
    
main()