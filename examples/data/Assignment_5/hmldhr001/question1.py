#Dhriven Hamlall

def display():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    x=input("Enter your selection:\n") # User makes a choice
    x=x.upper() # input will be in capitals
    return x # returning capital input

def main():
    choice="" # empty string 
    message="no message yet"
    fileNotFoundMessage="File not found"  #initialising
    
    while choice!="X": # while user did not try to exit using x 
        choice=display() #will continue to show menu option 
        if(choice=="E"):
            message=input("Enter the message:\n")
        elif(choice=="V"):
            print("The message is:",message)
        elif(choice=="L"):
            print("List of files: 42.txt, 1015.txt")
        elif(choice=="D"):
            fileName=input("Enter the filename:\n")
            if(fileName=="42.txt"):
                print("The meaning of life is blah blah blah ...")
            elif(fileName=="1015.txt"):
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print(fileNotFoundMessage) #basically if 42.txt or 1015.txt is not entered
                 
    else:
        print("Goodbye!")
                     
main()