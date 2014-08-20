"""BSS program
Jordan Kadish 15 April 2014"""
def BSS():
    mes = "no message yet"
    selection=""
    while selection!="X":
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection=input("Enter your selection:\n")
        selection=selection.upper()
        if selection=="E":
            mes = input("Enter the message:\n")
        elif selection=="V":
            print("The message is: "+mes)
        elif selection=="L":
            print("List of files: 42.txt, 1015.txt")
        elif selection=="D":
            file=input("Enter the filename:\n")
            if file=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            elif file!="42.txt" and file!="1015.txt":
                print("File not found")
        else:
            selection="X"
            print("Goodbye!")
if __name__=="__main__":
    BSS()