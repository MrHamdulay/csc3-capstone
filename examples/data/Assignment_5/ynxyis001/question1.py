#Question 1: Bulletin Board Systems (BBS) simulator
#Jennifer Yuan
#11 April 2014
 
def BBS(): #Choices
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

BBS() #Calling function
s = input("Enter your selection:\n") #Variable to be used in if functions


E="no message yet" #in case no message, but "V" or "v" selected
if s == "E" or s =="e":
    E = input("Enter the message:\n") #changing value of variable E, as there is now a message
    BBS()
    s = input("Enter your selection:\n") 


while s=="e" or s=="E" or s=="V" or s=="v" or s=="L" or s=="l" or s=="D" or s=="d": #retricting options
    E="no message yet" #in case no message, but "V" or "v" selected
    if s == "E" or s =="e":
        E = input("Enter the message:\n") #changing value of variable E, as there is now a message
        BBS()
        s = input("Enter your selection:\n")     
    
    if s == "V" or s =="v":
        print("The message is:", E)
    
    if s == "L" or s=="l":
        print("List of files: 42.txt, 1015.txt") #Only two options
    
    if s == "D" or s=="d":
        file_name = input("Enter the filename:\n")
        if file_name == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file_name == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    BBS() #Continuing asking until user e(X)its
    s= input("Enter your selection:\n")
            
if s == "X" or s=="x": #ending BBS()
    print("Goodbye!")     