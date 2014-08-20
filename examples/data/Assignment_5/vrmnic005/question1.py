#VRMNIC005
#assignment 5 question 1

def BBS():
    selection = ""
    message = "no message yet"
    while selection !="X" and selection!= "x": 
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection = input("Enter your selection: \n")

        if selection == "E" or selection == "e":
            message = input("Enter the message: \n")

        elif selection== "V"or selection== "v":
            print("The message is:", message)

        elif selection == "L" or selection == "l":
            print ("List of files: 42.txt, 1015.txt")

        elif selection == "D" or selection == "d":
            file_name = input("Enter the filename: \n")
            if file_name == "42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file_name == "1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print("File not found")
    print("Goodbye!")
BBS()
