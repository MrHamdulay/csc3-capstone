#deepak bhoojrajh
#q2 - 16 april 2014 - assignment 5

choice = ""
msg = "no message yet"

while choice != "X":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    s = input("Enter your selection:\n") 
    s = s.upper()
    
    if s == "E":
        msg = input("Enter the message:\n")
    elif s == "V":
        print("The message is:",msg) 
    elif s == "L":
        print("List of files: 42.txt, 1015.txt")
    elif s =="D":
        namef=input("Enter the filename:\n")
        if namef=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif namef=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work\nPass course\nBe happy")
        else:
            print("File not found")
                
        
        print("Goodbye!")