message="no message yet"
x="1"
while x=="1":
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    Selection=input("Enter your selection:\n").upper()
    
    if Selection=="V":
        print("The message is:",message)
    
    elif Selection=="E":
        y=input("Enter the message:\n")
        message=y 
   
    
    elif Selection=="L": 
        print("List of files: 42.txt, 1015.txt")
    
    
    elif Selection=="D":
        answer=(input("Enter the filename:\n"))
        
        if answer=="42.txt":
            print("The meaning of life is blah blah blah ...")
            
        elif answer=="1015.txt":
            print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")
            
        else:
            print("File not found")
        
    elif Selection == "X":
        print("Goodbye!")
        break
    
    
    

    