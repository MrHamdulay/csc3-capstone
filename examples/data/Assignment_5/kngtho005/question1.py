# question1.py
# a program to simulate a simple BBS with one stored message and 2 fixed files, as indicated in the output
# 14 April 2014
# Thomas Konigkramer

def bbs():
    selection = ""
    message = ""
    while str.upper(selection) != "X":
        """introduction"""
        print("Welcome to UCT BBS\n"
              "MENU")
    
        print("(E)nter a message\n"
              "(V)iew message\n"
              "(L)ist files\n"
              "(D)isplay file\n"
              "e(X)it")
    
        selection = input("Enter your selection:\n")
        
        if str.upper(selection) == "E":
            message = input("Enter the message:\n")
        
        elif str.upper(selection) == "E":
            message == ""
        
        if str.upper(selection) == "V":
            if message != "":
                print("The message is:", message)
            else:   
                print("The message is: no message yet")
                
        elif str.upper(selection) == "L":
            print("List of files: 42.txt, 1015.txt")
            
        elif str.upper(selection) == "D":
            filename = input("Enter the filename:\n")
            if filename == "42.txt":
                print("The meaning of life is blah blah blah ... ")
            elif filename == "1015.txt":
                print("Computer Science class notes ... simplified\n"
                      "Do all work\n"
                      "Pass course\n"
                      "Be happy")
            else:
                print("File not found")
    
    print("Goodbye!")
bbs()