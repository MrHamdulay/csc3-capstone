#SRXLUC001
#Lucy Sure
#program for quaetion 1 Assignment 5
Q="a"
message=""
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")    
    Q=input("Enter your selection:\n")
    if Q=='E' or Q=='e':
            message=input("Enter the message:\n")
    elif Q=='V' or Q=='v':
        if message=="":
            print("The message is: no message yet")
        else:
            print("The message is:",message)
    elif Q=='l'or Q=='L':
        print("List of files: 42.txt, 1015.txt")
    elif Q=='d' or Q=='D':
        Q2=input("Enter the filename:\n")
        if Q2=="42.txt":
                        print("The meaning of life is blah blah blah ...")
        elif Q2=="1015.txt":
                        print("Computer Science class notes ... simplified")
                        print("Do all work")
                        print("Pass course")
                        print("Be happy")  
        else:
            print("File not found")
    elif Q=="X" or Q=="x":
        print("Goodbye!")
        break
    
    
        
    
    
  