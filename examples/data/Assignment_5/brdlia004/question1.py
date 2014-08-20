#Liam Brodie
#UCT BBS
#12 April 2014
#BRDLIA004
#Assignment 5

""" UCT BBS System"""

txt15 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
Newmsg = "no message yet"

def mainMENU():
    """Shortcut for Menu start"""
    print("Welcome to UCT BBS")    
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    

def MENU():
    """Main Function of decision structures"""
    mainMENU()
    l = input("Enter your selection:\n").lower()  
    if l == "e":
        global Newmsg
        Newmsg = input("Enter the message:\n")
        MENU()
    if l == "v":
        print("The message is:", Newmsg)
        MENU()           
    if l == "l":
        print("List of files: 42.txt, 1015.txt")
        MENU()
    if l == "d":
        f = input("Enter the filename:\n")
        if f == "42.txt":
            print("The meaning of life is blah blah blah ...")
            MENU()
        elif f == "1015.txt":
            print(txt15)
            MENU()
        else:
            print("File not found")
            MENU()
    if l == "x":
        print("Goodbye!")


MENU()

