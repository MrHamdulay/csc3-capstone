message="no message yet"
option=""
while option!="x":
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it",sep="")
    option=input("Enter your selection:\n")
    
    if option=="e":
        message=input("Enter the message:\n")
    elif option=="v":
        print("The message is: ",message,sep="") 
    elif option=="l":
        print("List of files: 42.txt, 1015.txt",sep="")
    elif option=="d":
        filename=input("Enter the filename:\n")
        if filename=="42.txt":
            print("The meaning of life is blah blah blah ...",sep="")
        if filename=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy",sep="")
        if filename=="1016.txt":
            print("File not found",sep="")
print("Goodbye!",sep="")


        