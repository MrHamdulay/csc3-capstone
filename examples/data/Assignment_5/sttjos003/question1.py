x=0
message="no message yet"
while x<1:
    x=0
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    answer=input("Enter your selection:\n")
    answer=answer.upper()
    if answer=="E":
        message=input("Enter the message:\n")
        
    elif answer=="V":
        print("The message is:", message)
        
    elif answer=="L":
        print("List of files: 42.txt, 1015.txt")
        
    elif answer=="D":
        file=input("Enter the filename:\n")
        
        if file=="42.txt":
            print("The meaning of life is blah blah blah ...")
            
        elif file=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            
        else:
            print("File not found")
            
    elif answer=="X":
        print("Goodbye!")
        x=1
