"""Christopher Sterley
12/04/2014
Computer Science assignment"""
mess=""
l_sel=""
while l_sel!="x":
    print("Welcome to UCT BBS","\n","MENU","\n","(E)nter a message","\n","(V)iew message","\n","(L)ist files","\n","(D)isplay file","\n","e(X)it",sep="")
    sel=input("Enter your selection:\n")
    l_sel=str.lower(sel)
    if l_sel=="e":
        mess=input("Enter the message:\n")
    elif l_sel=="v":
        if mess=="":
            print("The message is: no message yet")
        else:
            print("The message is:",mess)
    elif l_sel=="l":
        print("List of files: 42.txt, 1015.txt")
    elif l_sel=="d":
        nam=input("Enter the filename:\n")
        if nam=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif nam=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
else:
    print("Goodbye!")