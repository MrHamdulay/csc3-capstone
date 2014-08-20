# Question 1 - Assignment 5
# Oliver Harrison
# 13 April 2014

def main():
    i=0
    x="42.txt"
    y="1015.txt"
    message="no message yet"
    while i==0:
        print ("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")
        selection=str.upper(input("Enter your selection: \n"))

        if selection=="E":
            message=input("Enter the message: \n")
        elif selection=="V":
            print("The message is:", message)
        elif selection=="L":
            print ("List of files: ",x,", ", y, sep="")
        elif selection=="D":
            filename=input("Enter the filename: \n")
            if filename==x:
                print("The meaning of life is blah blah blah ...")
            elif filename==y:
                print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")
            else:
                print("File not found")
        elif selection=="X":
            print("Goodbye!")
            break
main()

    