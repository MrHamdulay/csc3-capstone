"""Assignment 5, Question 1: a BBS"""

def Welcome():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

def FileHandle(file):
    """ a mock file system function to pretend to access the files of the
    UCT BBS"""
    if file == "1015.txt":
        print("Computer Science class notes ... simplified")
        print("Do all work\nPass course\nBe happy")
    elif file == "42.txt":
        print("The meaning of life is blah blah blah ...")
    else:
        print("File not found")

def UCTBBS():
    """A simple Bulletin Board System that displays a list of options to a user
    and acts upon the given command"""
    message = "no message yet" # the stored message
    Welcome()
    command = input("Enter your selection:\n").lower()
    while command != 'x': # break out of loop on boundary value 'x'
            if command in "evld":
                if command == 'e': # enter message command
                    message = input("Enter the message:\n")
                elif command == 'v': # view entered message command
                    print("The message is:", message)
                elif command == 'l': # view list of files command
                    print("List of files: 42.txt, 1015.txt")
                elif command == 'd': # display a file command
                    file = input("Enter the filename:\n")
                    FileHandle(file)
            Welcome()
            command = input("Enter your selection:\n").lower()
    print("Goodbye!")

if __name__ == '__main__':
    UCTBBS()