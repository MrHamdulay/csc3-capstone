#uct bbs
#kkmphele
#14/04/2014

def bbt():
    selection=""
    message=""
    while selection!="x":
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message\n"+"(V)iew message\n"+"(L)ist files\n"+"(D)isplay file\n"+"e(X)it")
        selection=input("Enter your selection:\n")
        selection=selection.upper()
       
        
        if selection=="E":
            message=input("Enter the message:\n")
        elif selection=="V":
            if len(message)==0:
                print("The message is: no message yet")
            else:
                print("The message is:",message)
        elif selection=="L":
            print("List of files: 42.txt, 1015.txt")
        elif selection=="D":
            file=input("Enter the filename:\n")
            if file=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file=="1015.txt":
                print("Computer Science class notes ... simplified\n"+"Do all work\n"+"Pass course\n"+"Be happy")
            elif file=="1016.txt":
                print("File not found")
            else: print("File not found")
        elif selection=="X":break
    print("Goodbye!")    
bbt()
    