
#BBS with one stored message and 2 fixed files
#Shivaan Motilal
#13/04/14

message=""
while True:
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

    x=input("Enter your selection:\n")
    
    if x=="V" or x=="v":             #Both capital and lowercase considered
            #if message!="":
             #   print("The message is:",message)
            if message=="":    
                print("The message is: no message yet")
            else:
                print("The message is:",message)    
    
    
    
    
    if x=="E" or x=="e":
        message=input("Enter the message:\n")  
        
        
        
    if x=="L" or x=="l":
        print("List of files: 42.txt, 1015.txt")
        
    if x=="D" or x=="d":
        fname=input("Enter the filename:\n")
        
        if fname=="42.txt" or fname=="1015.txt":
            infile=open(fname,"r")                #returns entire contents of file as a single string
            data=infile.read()
            print(data)
        
        else: print("File not found")
        
    if x=="X" or x=="x":
        print("Goodbye!")
        break
        
    


