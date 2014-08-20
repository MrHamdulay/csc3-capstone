# Yentl Naidu (NDXYEN001)
# 17 April 2014
# Assignment 5
# Question 1

# Asking person for input
y = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
# Create a variable
message =""

while(y!= "X" or  y!="x"): # When the input is not x, the program needs restart
    # If-Else/Elif statements when E,V,L & D are the inputs
    if(y=="E" or y=="e"):
        message = input("Enter the message:\n")
    elif(y =="V" or y == "v"):
        if (message==""):
            print("The message is: no message yet")
        else:
            print("The message is: "+message)
    elif(y=="L" or y=="l"):
        print("List of files: 42.txt, 1015.txt")
    elif(y=="D" or y=="d"):
        file_name=input("Enter the filename:\n")
        if(file_name=="42.txt"):
            print("The meaning of life is blah blah blah ...")
        elif(file_name=="1015.txt"):
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
     # When X/x is the input       
    elif(y=="x" or y=="X"):
        break
    y= input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
print("Goodbye!")
            