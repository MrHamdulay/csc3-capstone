"""interface program
Runako Muzwidzwa
13 April 2014"""

def bbs():
    i=""#so that i has a value
    text_msg=""
    while i in "EVLD" or "evld" :#to loop after each input
        print("Welcome to UCT BBS")
        a="(E)nter a message"
        b="(V)iew message"
        c="(L)ist files"
        d="(D)isplay file"
        e="e(X)it"
        print("MENU")
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        i=input("Enter your selection:\n")
        
        if i=="E" or i=="e":
            text_msg=input("Enter the message:\n")

        elif i=="V" or i=="v":
            if text_msg=="":
                print("The message is: no message yet")
            else:
                print("The message is:",text_msg)
        
        elif i=="L" or i=="l":
            print("List of files: 42.txt, 1015.txt")
        elif i=="D" or i=="d":
            g=input("Enter the filename:\n")
            if g=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif g=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else :
                print("File not found")
        elif i=="X" or i=="x":
            print("Goodbye!")
            break
bbs()