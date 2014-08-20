#DenishaRamaloo
#Question1
#assignment5

message="no message yet" 
choice=""

while choice!="X" and choice!="x": 
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    

    choice=input("Enter your selection:\n")

    if choice=="e" or choice=="E":
        message=input("Enter the message:\n")
        
    
    elif choice=="v" or choice=="V":
        print("The message is:", message)
        
               

    elif choice=="L" or choice=="l":
        print("List of files: 42.txt, 1015.txt")
        
    
    elif choice=="d" or choice=="D":
        dec=input("Enter the filename:\n")
        if dec=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif dec=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else: 
            print("File not found") 
            
print("Goodbye!")
