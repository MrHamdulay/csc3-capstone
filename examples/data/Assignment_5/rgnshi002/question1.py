#Shivam Ragoonaden
#UCT BBS


print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
m = ""   #Initialise message as blank for "V"
s = input("Enter your selection:\n")

while s.upper() != "X":   #Keep repeating until user has entered "X"
        if s.upper() == "E":
                m = input("Enter the message:\n")
                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")   
                s = input("Enter your selection:\n")        #Restart the Menu
    
        if s.upper() == "V":
                if m != "": #Check if a message has been entered yet
                        print("The message is: " + m)
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it") 
                        s = input("Enter your selection:\n")            
                else:
                        print("The message is: no message yet")
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")     
                        s = input("Enter your selection:\n")    
                        
        if s.upper() == "L":
                print("List of files: 42.txt, 1015.txt")
                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")      
                s = input("Enter your selection:\n")                
                
        if s.upper() == "D":
                f = input("Enter the filename:\n")     #Test for each file and print appropriate line
                if f == "42.txt": 
                        print("The meaning of life is blah blah blah ...")
                        
                elif f == "1015.txt":
                        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                else:
                        print("File not found")
                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")     
                s = input("Enter your selection:\n")                
                
else: #When user enters "X", while loop executes else statement
        
        print("Goodbye!")