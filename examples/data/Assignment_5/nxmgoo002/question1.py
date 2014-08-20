'''public Bulletin Board System
Nxumalo Goodman
14 April 2014'''

def bbs():
    start = 0
    message = ("no message yet")
    while start != 1:
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        
        
        selection = input("Enter your selection:\n")
        if selection == 'x' or selection == 'X':
            print("Goodbye!")
            start += 1
        elif selection == 'e' or selection == 'E' :
            message = input("Enter the message:\n")
        elif selection == 'v' or selection == 'V':
            print("The message is:", message)
        elif selection == 'l' or selection == 'L':
            print("List of files: 42.txt, 1015.txt")
        elif selection == 'd' or selection == 'D':
            filename = input("Enter the filename:\n")
            if filename == '42.txt':
                print("The meaning of life is blah blah blah ...")
            elif filename == '1015.txt':
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print("File not found")
    
bbs()