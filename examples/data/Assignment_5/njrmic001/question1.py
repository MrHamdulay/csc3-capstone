#Question1.py
#A Bulletin Board System program
#Author: Michelle Njoroge
#15 April 2014
    
def main():
    x=" " #intialize the value of x
    message=" " #initialize the value of message

#iterate through the loop until the user types in "x" or "X" (To exit)
    while x!="X" or x!="x":
        print ("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection=input("Enter your selection:\n")
        if selection=="E" or selection=="e":
            message=input("Enter the message:\n")
        if selection=="V" or selection=="v":
            if message==" ": #The user has not entered a message yet
                print("The message is: no message yet")
            else:
                print ("The message is:", message)
        if selection=="l":
            print("List of files: 42.txt, 1015.txt")
        if selection=="d":
            x=input("Enter the filename:\n")
            if x=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif x=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print("File not found")
        if selection=="x" or selection=="X":
            break #exit the loop
    print("Goodbye!")
            
main()







