message = ""
def messege(sel):
    global message
    message += sel
    return message


def MENU():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection=input("Enter your selection:\n")
    return selection
    
def BBM():  
    run = False
    while not run:    
        selection = MENU()
        if selection == "e" or selection == "E":
            sel = input("Enter the message:\n")
            messege(sel)
        elif selection == "v" or selection == "V":            
            if message =="":
                print("The message is: no message yet")
            else:
                print("The message is:",message)
        elif selection == "l" or selection == "L":
            print("List of files: 42.txt, 1015.txt")
            
        elif selection == "d" or selection == "D":
            name = input("Enter the filename:\n")
            if name == "1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            elif name == "42.txt":
                print("The meaning of life is blah blah blah ...")
            else:
                print("File not found")
                
        elif(selection == "x" or selection == "X"):
            print("Goodbye!")
            run = True
    
BBM()   