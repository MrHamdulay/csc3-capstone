"""UCT BBS
nelisile mkhwebane
14/04/2014"""

#initialise the message to default  message and the selection to an empty string

M="no message yet"
selection=""

# the program has to run over and and over until the selection entered is "X")

while (selection!="X"):
        print("Welcome to UCT BBS")
        print ("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        
        #get the selection from user
        selection = input ("Enter your selection:\n")
        
        # the input has to be in capital letters
        
        selection= selection.upper()
        
        # control functions, to get desired outputs.

        if selection=="E":
                M = input("Enter the message:\n")
        elif selection == "V":
                print("The message is:", M )
        elif selection =="D":
                filename=input("Enter the filename:\n")
                if filename == "42.txt":
                        print("The meaning of life is blah blah blah ...")
                elif filename == "1015.txt":
                        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                else:
                        print("File not found")
        elif selection =="L":
                print("List of files: 42.txt, 1015.txt")
        
        if selection =="X":
                print("Goodbye!")