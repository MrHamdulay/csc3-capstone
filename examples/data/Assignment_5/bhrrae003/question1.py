#Program to simulate a simple BBS with one stored message and 2 fixed files
#Raeesa Behardien
#17 April 2014

#Definitions
#display menu
def main_menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")   
main_menu()

#Select E

message = ""
files = ["42.txt", "1015.txt"]

while True:
    select = input("Enter your selection:" '\n')
    select = select.lower()
#E
    if select == "e":
        message = input("Enter the message:" '\n')
        main_menu()
#V    
    elif select == "v":
        if message == "":
            print("The message is: no message yet")
        else: 
            print("The message is:", message)
        main_menu()
#L    
    elif select == "l":
        print("List of files: ", files[0], ", ", files[1],sep="")
        main_menu()
#D    
    elif select == "d":
        file = input("Enter the filename:" '\n')
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified" '\n' "Do all work" '\n' "Pass course" '\n' "Be happy")
        else:
            print("File not found")        
        main_menu()
#X
    elif select == "x":
        print("Goodbye!")
        break

    
 