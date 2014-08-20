message="no message yet"
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    
    files = ["42.txt","1015.txt"]
    selection =(input("Enter your selection:\n")).upper()
    
    if selection=="V" :
            print("The message is:",message)
            
        
    elif selection=="E":
        message = (input("Enter the message:\n"))
        
    elif selection=="V" and message!="no message yet":
        print("The message is:" , message)
        
    
    elif selection=="L":
        print("List of files:",files[0]+", "+files[1])
    
    elif selection=="D":
        file_name=input("Enter the filename:\n")
        if file_name=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        
        elif file_name=="42.txt":
            print("The meaning of life is blah blah blah ...")
            
        else:
            print("File not found")
            
    elif selection=="X":
        print("Goodbye!")
        break