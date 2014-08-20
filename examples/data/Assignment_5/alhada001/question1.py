#Adam Alhadeff ALHADA001

print("Welcome to UCT BBS\n","MENU\n","(E)nter a message\n","(V)iew message\n","(L)ist files\n","(D)isplay file\n","e(X)it",sep = "")#prompts user
letter = input("Enter your selection:\n")#user enters a value
message = ""   
while letter.upper() != "X":#Data validation
    
    #Series of if statements that are dependant on the users input
    #Each if statement executes what is stipulated in the message tha prompted the user
    if letter.upper() == "E":
        message = input("Enter the message:\n")      
 
    elif letter.upper() == "V":
        if message == "":
            print("The message is: no message yet")
        else:
            print ("The message is:",message)        
         
    elif letter.upper() == "L":
        print ("List of files: 42.txt, 1015.txt")
     
    elif letter.upper() == "D":
        file = input("Enter the filename:\n")
        
        if file == "42.txt":
            fone = open(file,"r")
            print(fone.read())
        elif file == "1015.txt":
            fone = open (file,"r")
            print(fone.read())
        
        #File not found        
        else:
            print("File not found")
    print("Welcome to UCT BBS\n","MENU\n","(E)nter a message\n","(V)iew message\n","(L)ist files\n","(D)isplay file\n","e(X)it",sep = "")
    letter = input("Enter your selection:\n")    
       
print("Goodbye!")