#Tofunmi Olagoke
#OLGMOF001
#15 April 2014
#Program of UCT BBS

print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")   
selection=input("Enter your selection:\n")

message="no message yet" 

while not selection=="x" or selection=="X":
    #selection E
    if selection=="E" or selection=="e":
        message=input("Enter the message:\n")
    #selection v
    elif selection=="V" or selection=="v":
            print("The message is:", message)
    #selection l
    elif selection=="L" or selection=="l": 
            print("List of files: 42.txt, 1015.txt") 
    #selection d
    elif selection=="D" or selection=="d":
            file=input("Enter the filename:\n")
            if file=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy") 
            else:
                print("File not found")
                
    #Breaks out of loop for exit       
    elif selection=="X" or selection=="x":
        print("Goodbye!")
        break
        

    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")   
    selection=input("Enter your selection:\n")

#if you selection is X from the beginning   
if selection=="X" or selection=="x":
    print("Goodbye!")

