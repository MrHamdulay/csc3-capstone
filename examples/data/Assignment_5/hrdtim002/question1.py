"""UCT bulletin board system
Tim Hardie
16-4-14"""

# creates menu
def menu ():
    print ("Welcome to UCT BBS")
    print ("MENU")
    print ("(E)nter a message")
    print ("(V)iew message")
    print ("(L)ist files")
    print ("(D)isplay file")
    print ("e(X)it")
    choice = input ("Enter your selection:\n")
    return choice


if __name__ == '__main__':
    choice = menu()
    message = "no message yet"
    # invoking whatever function the user enters
    while (choice != 'X' and choice != 'x'):
        
        # enter a message
        if (choice == 'E' or choice == 'e'):
            message = input ("Enter the message:\n")
        
        # view message if it exists
        elif (choice == 'V' or choice == 'v'):
            print ("The message is:",message)
        
        # list files
        elif (choice == 'L' or choice == 'l'):
            print("List of files: 42.txt, 1015.txt")
        
        # display chosen file if it exists
        elif (choice == 'D' or choice == 'd'):
            file = input ("Enter the filename:\n")
            if (file == '42.txt'):
                print ("The meaning of life is blah blah blah ...")
            elif (file == '1015.txt'):
                print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print ("File not found")
        
        # gets user's next choice
        choice = menu()
    print ("Goodbye!")