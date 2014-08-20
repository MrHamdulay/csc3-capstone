"""
Prashanth Sridharan
SRDPRA001
Question 01
Assignment 5
"""
"""
Variable names being used here"""
#i: is is the variable name for the choice of input. 
#file is the variable name for the file to be selected/executed.

i = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
message=""


if (i=="E" or i=="e"):
    message=input("Enter the message:\n")
elif (i=="V" or i=="v"):
    if(message!=""):
        print("The message is: "+message) #In case there is no message
    else:
        print("The message is: no message yet")
elif (i=="L" or i=="l"):
    print("List of files: 42.txt, 1015.txt")
elif (i=="D" or i=="d"):
    file = input("Enter the filename:\n")
    if (file=="42.txt"):
        print("The meaning of life is blah blah blah ...")
    elif (file=="1015.txt"):
        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
    else:
        print("File not found")
   #this part is incase the user did not quit the program
if(i!="X" and i!="x"):        
    i = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    
    while(i!="X" and i!="x"): #The loop stage if the user did not quit the program
        if (i=="E" or i=="e"):
            message=input("Enter the message:\n")
        elif (i=="V" or i=="v"):
            if(message!=""):
                print("The message is: "+message)
            else:
                print("no message yet")
        elif (i=="L" or i=="l"):
            print("List of files: 42.txt, 1015.txt")
        elif (i=="D" or i=="d"):
            file = input("Enter the filename:\n")
            if (file=="42.txt"):
                print("The meaning of life is blah blah blah ...")
            elif (file=="1015.txt"):
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print("File not found") #For invalid file names
        i = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")    
    print("Goodbye!") #This is the statement that will be executed when the user quits the program or the loop
else:
    print("Goodbye!")
