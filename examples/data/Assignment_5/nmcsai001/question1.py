"""Saijil Nemchund
Question 1 
16 April 2014"""



message="no message yet"
selection=""  #introducing the string to the program


while selection!="X" and selection!="x":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    
    

    selection=input("Enter your selection:\n")

    if selection=="e" or selection=="E": #if you enter a lowercase, it converts it to upper case
        message=input("Enter the message:\n")

        
        
    
    elif selection=="v" or selection=="V":
        print("The message is:", message)
        
               

    elif selection=="L" or selection=="l":
        print("List of files: 42.txt, 1015.txt")
        
    
    
    elif selection=="d" or selection=="D":
        dec=input("Enter the filename:\n")
        if dec=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif dec=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else: 
            print("File not found")
            
print("Goodbye!")
