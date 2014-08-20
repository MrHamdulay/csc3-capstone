""" Bulletin Board Systems
Tameryn Pillay
16 April 2014 """


 
def view_message():
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")


def choice(a):
    if a == "V" or a == "v":
        print("The message is: no message yet")
        menu()
        
        
    elif a == "D" or a == "d":
            g = input("Enter the filename:\n")
            if g == "42.txt":
                print("The meaning of life is blah blah blah ...")
                menu()
            elif g == "1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                menu()
            else:
                print("File not found")
                menu()    
        

    elif a == "E" or a == "e":
        b = input("Enter the message:\n")
        view_message()
        c = input("Enter your selection:\n")
        if c == "V" or c == "v":
            print("The message is:",b)
            menu()
        else:
            choice(c)
            
    elif a == "L" or a == "l":
        print("List of files: 42.txt, 1015.txt")
        menu()
        

      
def menu():
    view_message()
    selection = input("Enter your selection:\n")

    if selection == "X" or selection == "x":
        print("Goodbye!") 
    else:
        choice(selection)   
    
menu()