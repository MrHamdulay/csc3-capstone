#Siphesihle Cele
#assignment 5
#program that simulates a BBS interface.

select=""  
message=("no message yet")  #statement that showes that no message exists as yet.
while select!="X":  #while loop to print menu repeated times until a certain statement is reached.
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")                 #print statements to display on screen
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    select=input("Enter your selection:\n").upper()  #input being capitalized
    if select=="E":   
        message=input("Enter the message:\n")
    elif select=="V":
        print("The message is:",message)
    elif select=="L":
        print("List of files: 42.txt, 1015.txt")
    elif select=="D":
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
    print("Goodbye!") 
    