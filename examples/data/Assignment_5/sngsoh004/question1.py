#SNGSOH004
#Assignment 5
#Question1

option = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
message=""
#Now to perform the desired task
if (option=="E" or option=="e"):
    message=input("Enter the message:\n")
elif (option=="V" or option=="v"):
    if(message!=""):
        print("The message is: "+message) #In case there is no message
    else:
        print("The message is: no message yet")
elif (option=="L" or option=="l"):
    print("List of files: 42.txt, 1015.txt")
elif (option=="D" or option=="d"):
    file = input("Enter the filename:\n")
    if (file=="42.txt"):
        print("The meaning of life is blah blah blah ...")
    elif (file=="1015.txt"):
        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
    else:
        print("File not found")
   #If they did not choose to exit the program: 
if(option!="X" and option!="x"):        
    option = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    #Ask to perform a new function
    
    while(option!="X" and option!="x"): #If they decided not to quit, again, do the following:
        if (option=="E" or option=="e"):
            message=input("Enter the message:\n")
        elif (option=="V" or option=="v"):
            if(message!=""):
                print("The message is: "+message)
            else:
                print("no message yet")
        elif (option=="L" or option=="l"):
            print("List of files: 42.txt, 1015.txt")
        elif (option=="D" or option=="d"):
            file = input("Enter the filename:\n")
            if (file=="42.txt"):
                print("The meaning of life is blah blah blah ...")
            elif (file=="1015.txt"):
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print("File not found")    
        option = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")    
    print("Goodbye!") #This command will only be executed once the while loop has been terminated, which will only occur when the user states they want to exit
else:
    print("Goodbye!")
