#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014/04/16
#Function       : To print a text based graph of a mathematical function
#Title          : Question 4
def BBSMenu(): #lists the menu and requests the user for an input
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    selection = input("Enter your selection:\n")
    return selection.upper() #ensures users input is a upper case letter

user_input = BBSMenu() 

message = "no message yet"

while user_input != "X":  #while the user hasn't pressed exit
    if user_input == "E":
        message = input("Enter the message:\n")

    elif user_input == "V":
        print("The message is:", message)

    elif user_input == "L":
        print("List of files: 42.txt, 1015.txt")

    elif user_input == "D":
        file_name = input("Enter the filename:\n")

        if file_name == "42.txt":
            print("The meaning of life is blah blah blah ...")

        elif file_name == "1015.txt":

            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")

        else:
            print("File not found")

    user_input = BBSMenu()

        
    
print("Goodbye!")
