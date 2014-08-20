"""A5Q1 - BBS
Keegan Crankshaw
14/4/2014"""

message = "no message yet"

def startup():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection = (input("Enter your selection:\n"))[0].upper()
    
    if selection == "E":
        EnterMessage()        
    elif selection == "V":
        print("The message is: " + message)
        startup()        
    elif selection == "L":
        print("List of files: 42.txt, 1015.txt")
        startup()
    elif selection == "D":
        selection = input("Enter the filename:\n")
        FetchFile(selection)
    elif selection == "X":
        print("Goodbye!")


def EnterMessage():
    global message 
    message = input("Enter the message:\n")
    startup()
    
def FetchFile(file):
    if file == "42.txt":
        print("The meaning of life is blah blah blah ...")
        startup()
    elif file == "1015.txt":
        print("Computer Science class notes ... simplified")
        print("Do all work")
        print("Pass course")
        print("Be happy")
        startup()
    else:
        print("File not found")
        startup()      

    
if __name__ == "__main__":
    startup()
    