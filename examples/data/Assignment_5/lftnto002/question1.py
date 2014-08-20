"""Program that simulates simple public Bulletin Board Systems (BBS)
   Bridgette Lefatsa
   LFTNTO002
   18 April 2014"""
t= True
message=""
while t:
    print( "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    selection= input("Enter your selection:\n")
    selection= selection.upper()


    if selection =="E":
        message=input("Enter the message:\n")
    
    elif selection =="V":
        if message:
            print("The message is:",message)
        else:
            print("The message is: no message yet")
    
    elif selection =="L":
        print("List of files: 42.txt, 1015.txt")
    
    elif selection =="D":
        filename=input("Enter the filename:\n")
        if (filename=="42.txt") or (filename=="1015.txt"):
            file = open(filename, 'r')
            print (file.read(),end="")
        else:
            print("File not found") 
        
    elif selection =="X":
        print("Goodbye!")
        t=False
    
    