# Author : Rayaan Fakier FKRRAY001
# Date : 14 - 04 - 2014
# Program that simulates Bulletin Board Systems (BBS)

def main():
    message_list = [] # Will contain message 
    files_list = ["42.txt", "1015.txt"]
    choice = "" # Initialize BBS
    while choice != "n":
        menu() # Calls MENU display everytime
        choice = input("Enter your selection:\n")
        if choice == "E" or choice == "e":
            message_input = input("Enter the message:\n")
            message_list.append(message_input)
        if choice == "V" or choice == "v":
            if len(message_list) == 0: # Check if message has been entered
                print("The message is: no message yet")
            else:
                print("The message is:", message_list[0])
        if choice == "L" or choice == "l":
            print("List of files:",files_list[0] +",", files_list[1])
        if choice == "D" or choice == "d":
            choose_file = input("Enter the filename:\n")
            if choose_file == files_list[0]:
                print("The meaning of life is blah blah blah ...")
            elif choose_file == files_list[1]:
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print("File not found")
        if choice == "X" or choice == "x": # Exiting
            print("Goodbye!")
            break
# Function just to hold MENU -- easier and 'cleaner' to call
def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
main()