# Program to simulate a Bulletin Board System (BBS)
# Nomsa Gamedze
# 14 April 2014

saved = False

def BBS():
    global saved
    global message
    print("Welcome to UCT BBS", "MENU", "(E)nter a message", "(V)iew message" , "(L)ist files" , "(D)isplay file" , "e(X)it" , sep='\n')
    choice = input("Enter your selection:"'\n')
    choice = choice.upper()
    if choice != "X":
        if choice == "E":
            message = input("Enter the message:"'\n')
            saved = True
            BBS()
        if choice == "V":
            if saved:
                print("The message is:", message)
                BBS()
            if not saved:
                print("The message is: no message yet")
                BBS()
        if choice == "L":
            print("List of files: 42.txt, 1015.txt")
            BBS()
        if choice == "D":
                file = input("Enter the filename:"'\n')
                if file == "42.txt" or file == "1015.txt":
                        file = open(file)
                        file_text = file.read()
                        print(file_text)
                        BBS()
                else:
                    print("File not found")
                    BBS()
    if choice == "X":
        print("Goodbye!")

BBS()