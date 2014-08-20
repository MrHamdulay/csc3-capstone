a=""
x=""

while x!="x" or x!="X":
    print("Welcome to UCT BBS")
    print('MENU')
    print("(E)nter a message")
    print('(V)iew message')
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    x=input("Enter your selection:\n")    

    if x=="E" or x=="e":
        a=input("Enter the message:\n")
        continue      
        
    if x=="v" or x=="V":
        if a=="":
            print("The message is: no message yet")
        else:
            print("The message is:", a)
            
    if x=="l" or x=="L":
        print("List of files: 42.txt, 1015.txt")
        
    if x=="d" or x=="D":
        b=input("Enter the filename:\n")
        if b=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif b=="1015.txt":
            print("Computer Science class notes ... simplified", "Do all work", "Pass course", "Be happy", sep="\n")
        else:
            print("File not found")
           
    if x=="x" or x=="X":
        print("Goodbye!")
        break   
