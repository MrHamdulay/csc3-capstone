#Author: Rofhiwa Liphauphau
#Date: 16 April 2014
#Program for an interface

z=("no message yet")#creating a variable z to store an input further in the program
while True: #algorithm repeats until user wants to exit
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it") 
    x= input("Enter your selection:\n") #prompt the user to enter a selection based on the list given
    if x=="V" or x=="v":
        a=z #This gives the value of the message entered
        print("The message is:",a)
    if x=="E" or x=="e":
            z=input("Enter the message:\n")    
    elif x=="X" or x=="x":
        print("Goodbye!")
        break #break out of the loop when the user prompts it to do so
    elif x=="L" or x=="l":
        print("List of files: 42.txt, 1015.txt")
    elif x=="D" or x=="d":
        y=input("Enter the filename:\n")
        if y=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif y=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")

