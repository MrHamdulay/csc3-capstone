sel=""
mes=""
txt1="The meaning of life is blah blah blah ..."
txt2="Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
while(sel!='X' and sel !='x'):
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    sel=input("Enter your selection:\n")
    if(sel=='e'):
        mes=input("Enter the message:\n")    
    if(sel=='v'):
        if(mes!=""):
            print("The message is:",mes)
        else:
            print("The message is: no message yet")
    if(sel=='l'):
        print("List of files: 42.txt, 1015.txt")
    if(sel=='d'):
        filename=input("Enter the filename:\n")
        if(filename=="42.txt"):
            print(txt1)
        elif(filename=="1015.txt"):
            print(txt2)
        else:
            print("File not found")
print("Goodbye!")


