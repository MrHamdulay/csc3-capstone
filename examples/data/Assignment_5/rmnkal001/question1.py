#Kalind Ramnarayan
#15 April 2014

def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

def file_1():
    print("The meaning of life is blah blah blah ...") #42.txt
def file_2():
    print("Computer Science class notes ... simplified") #1015.txt
    print("Do all work")
    print("Pass course")
    print("Be happy")
    
    

message="no message yet"

while True:
    menu()
    task=input("Enter your selection:\n")
    if task=="E" or task=="e":
        message=input("Enter the message:\n")
    
    elif task=="v" or task=="V":
        print("The message is:", message)
    
    elif task=="l" or task=="L":
        print("List of files: 42.txt, 1015.txt")
    
    elif task=="D" or task=="d":
        filename=input("Enter the filename:\n")
        if filename=="1015.txt":
            file_2()
        elif filename=="42.txt":
            file_1()
        else:
            print("File not found")
        
        
    elif task=="x" or task=="X":
        print("Goodbye!")
        break
   