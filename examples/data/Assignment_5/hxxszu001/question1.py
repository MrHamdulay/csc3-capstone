#UCT BBS
#Annie's programme!

msg="no message yet"
x="1"
while x=="1":
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    Select=input("Enter your selection:\n").upper()
    
    if Select=="V":
        print("The message is:",msg)
    
    elif Select=="E":
        y=input("Enter the message:\n")
        msg=y 
   
    
    elif Select=="L": 
        print("List of files: 42.txt, 1015.txt")
    
    
    elif Select=="D":
        ans=(input("Enter the filename:\n"))
        
        if ans=="42.txt":
            print("The meaning of life is blah blah blah ...")
            
        elif ans=="1015.txt":
            print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")
            
        else:
            print("File not found")
        
    elif Select == "X":
        print("Goodbye!")
        break
    
    
    

    