"""program of a simple Bulletin Board System
Shane Robinson
17 April 2014"""

ans = ""
ans1 = ""
while ans!='X':
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    print("Enter your selection:")
    ans = input()
    ans = ans.upper()
    if ans=='E':
        print("Enter the message:")
        ans1 = input()
    if ans=='V':
        if ans1=="":
            print("The message is: no message yet")
        else:
            print("The message is:",ans1)        
    if ans=='L':
        print("List of files: 42.txt, 1015.txt")
    if ans=='D':
        print("Enter the filename:")
        ans2 = input()
        if ans2=='42.txt':
            print("The meaning of life is blah blah blah ...")
        elif ans2=='1015.txt':
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
else:
    print("Goodbye!")