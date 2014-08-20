#Tashfia Amin #AMNTAS003 #Due:17 April 2014

#create variables for later use
selection=""
message=""

#false variables to end program
X=False
x=False

#menu will print until the user quits
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection=input("Enter your selection: \n")

    if selection=="E" or selection=="e":    #allows user to store a message that can be viewed later
        message=input("Enter the message: \n")
        
    if selection=="V" or selection=="v":    #prints previously entered message or lets user know there is no stored message
        if message=="":
            print("The message is: no message yet")
        else:
            print("The message is:", message)
        
        
    if selection=="L" or selection=="l":    #creates a list of files that can be opened
        print("List of files: 42.txt, 1015.txt")
        
    if selection=="D" or selection=="d":    #allows for viewing of list of files
        filename=input("Enter the filename: \n")
        if filename=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename=="1015.txt":
            print("Computer Science class notes ... simplified \n", "Do all work \n", "Pass course \n", "Be happy", sep="")
        else: print("File not found")
        
    if selection=="X" or selection=="x":    #ends programme
        print("Goodbye!")
        break