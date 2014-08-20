#simpleBBS
#Devaksha Pillay
#15 April 2014

#function to show potential options to the user
def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
menu()
x = input("Enter your selection:\n")

#for all options except exit
while x == "e" or x == "E" or x == "V" or x == "v" or x == "L" or x == "l" or x == "d" or x == "D":
    
    if x == "v" or x == "V":
        print("The message is: no message yet")
        
    elif x == "E" or x == "e":
        y = input("Enter the message:\n")
        menu()
        x = input ("Enter your selection:\n")
        #v continues from e
        if x == "V" or x == "v":
            print("The message is:",y)
        elif x == "L" or x == "l":
                print("List of files: 42.txt, 1015.txt")
        elif x == "D" or x == "d":
                z = input ("Enter the filename:\n")
                if z == "42.txt":
                    print("The meaning of life is blah blah blah ...")
                elif z == "1015.txt":
                    print("Computer Science class notes ... simplified")
                    print("Do all work")
                    print("Pass course")
                    print("Be happy")
                else:
                    print("File not found")                
            
    elif x == "L" or x == "l":
        print("List of files: 42.txt, 1015.txt")
    
    elif x == "D" or x == "d":
        z = input ("Enter the filename:\n")
        if z == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif z == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
            
    menu()
    x = input("Enter your selection:\n")
    
if x == "X" or x == "x":
    print("Goodbye!")