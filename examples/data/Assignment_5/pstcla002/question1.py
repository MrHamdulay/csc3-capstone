"""simple BBS
Claudia Pastellides
15 April 2014"""
message =''
while True: # for all values that are true this expression will repeat
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it ")
    selection=input("Enter your selection:\n")
    
    if selection=="E" or selection=="e": #If user wants to enter a message, both small and capital included
            message+= input("Enter the message:\n")
        
    elif selection=="V" or selection=="v":
        if message =='':
            print("The message is: no message yet")
        else:   
            print("The message is:",message)
    
    
    elif selection== "L" or selection== "l":
        print("List of files: 42.txt, 1015.txt")
    
    elif selection=="D" or selection=="d":
        file=input("Enter the filename:\n")
        if file=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found") # for when there is no such file
    
    elif selection=="X" or selection=="x":break #loop breaks if exit is selected
print("Goodbye!")