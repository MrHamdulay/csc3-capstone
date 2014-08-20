#Kieran Reilly, RLLKIE001
#Assignment5, Question1
#BBS
#13/04/14

message = ""
file1 = "42.txt"
file2 = "1015.txt"
fileName = ""
choice = ""

while choice != "x" or choice != "X":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice = input("Enter your selection: \n")
    
    if(choice == "x" or choice =="X"):
        print("Goodbye!")
        break
    elif( choice == "e" or choice == "E"):
        message = input("Enter the message: \n")
    elif(choice == "v" or choice == "V"):
        if(message == ""):
            print("The message is: no message yet")
        else:
            print("The message is: " + message)
    elif(choice == "l" or choice == "L"):
        print("List of files: 42.txt, 1015.txt")
    elif(choice == "d" or choice =="D"):
        fileName = input("Enter the filename: \n")
        if( fileName == file1):
            print("The meaning of life is blah blah blah ...")
        elif(fileName == file2):
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        elif(fileName != file1 or fileName != file2):
            print("File not found")
            