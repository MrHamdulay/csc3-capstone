# AUTHOR:PERCIVAL MUNHUWAANI
# DATE  :15/04/2014
# MENU BASED PROGRAM TO THAT SIMULATES A SIMPLE BBS 
def main():
    message = "no message yet"  #This is when no message has been entered yet
    while input!="x":
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        option=input("Enter your selection:\n")
        if option=="E" or option=="e":
            message=input("Enter the message:\n")
        if option=="V" or option=="v":
            print("The message is:",message)
        if option=="L" or option=="l":
            print("List of files: 42.txt, 1015.txt")
        if option=="D" or option=="d":
            file_nam=input("Enter the filename:\n")
            if file_nam=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file_nam=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print("File not found") #this is when the file has not been found
        if option=="X"or option=="x":
            print("Goodbye!")
            break    #stop the loop
main()
        
        