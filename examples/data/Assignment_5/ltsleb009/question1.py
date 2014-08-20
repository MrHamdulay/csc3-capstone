#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Taylor
#
# Created:     13/04/2014
# Copyright:   (c) Taylor 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def menu():
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")


def main():

    while True:

        menu()
        message = ""
        selection = input("Enter your selection:")
        if selection.upper() == "X":
            break
        elif selection.upper() == "E":
            message = input("Enter the message")
            menu()
            selection = input("Enter your selection:")
        elif selection.upper() == "V":
            if message:
                print("The message is: {0}".format(message))
                menu()
                selection = input("Enter your selection:")
            else:
                print("No message yet")
                menu()
                selection = input("Enter your selection:")
        elif selection.upper() == "L":
            print("List of files: 42.txt, 1015.txt") #TBC
            menu()
            selection = input("Enter your selection:")
        elif selection.upper() == "D":
            file_name = input("Enter the filename:\n")
            display = (file_name, "r")
            menu()
            selection = input("Enter your selection:")

    print("Goodbye!")
if __name__ == '__main__':
    main()
