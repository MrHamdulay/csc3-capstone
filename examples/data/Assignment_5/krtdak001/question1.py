message = None

def BBS():
    end = False
    while end != True:
        
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file") 
        print("e(X)it")
    
        global message    #MAKE THE VARIABLE GLOBAL TO REUSE FUNCTION
        
        a = userinput = input("Enter your selection:\n")     #USER SELECTION INPUT
        
        #MEAT OF DIS PROGRAM
        if a == "E" or a == "e":
            message = input("Enter the message:\n")
        elif a == "V" or a == "v":
            if message == None:
                print("The message is: no message yet")
            else:
                print("The message is:", message)
        elif a == "L" or a == "l":
            print("List of files: 42.txt, 1015.txt")
        elif a == "D" or a == "d":
            b = filename = input("Enter the filename:\n")
            if b == "42.txt":
                print("The meaning of life is blah blah blah ...")
            elif b == "1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print("File not found")
        elif a == "X" or a == "x":
            print("Goodbye!")
            end = True
BBS()