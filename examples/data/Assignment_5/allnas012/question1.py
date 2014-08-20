def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")


def main():
    menu()
    selection=input("Enter your selection:\n")
    if selection=="V" or selection=="v":
        print("The message is: no message yet")
        menu()
        selection=input("Enter your selection:\n")    
    if selection=="E" or selection=="e":
        mes=input("Enter the message:\n")
        menu()
        selection=input("Enter your selection:\n")
    if selection=="V" or selection=="v":
        print("The message is:",mes)
        menu()
        selection=input("Enter your selection:\n")
    if selection=="L" or selection=="l":
        print("List of files: 42.txt, 1015.txt")
        menu()
        selection=input("Enter your selection:\n")
    if selection=="D" or selection=="d":
        filename=input("Enter the filename:\n")
        if filename=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            menu()
            selection=input("Enter your selection:\n")
        else:
            print("File not found") 
            menu()
            selection=input("Enter your selection:\n")
            if selection=="D" or selection=="d":
                    filename=input("Enter the filename:\n")
                    if filename=="42.txt":
                        print("The meaning of life is blah blah blah ...")
                    elif filename=="1015.txt":
                        print("Computer Science class notes ... simplified")
                        print("Do all work")
                        print("Pass course")
                        print("Be happy")
                        menu()
                        selection=input("Enter your selection:\n")
                        if selection=="D" or selection=="d":
                                filename=input("Enter the filename:\n")
                                if filename=="42.txt":
                                    print("The meaning of life is blah blah blah ...")
                                elif filename=="1015.txt":
                                    print("Computer Science class notes ... simplified")
                                    print("Do all work")
                                    print("Pass course")
                                    print("Be happy")
                                menu()
                                selection=input("Enter your selection:\n")
                                if selection=="X" or selection=="x":
                                        print("Goodbye!")                                
    
    elif selection=="X" or selection=="x":
        print("Goodbye!")
       
                
main()