x=""
print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")
user = input("Enter your selection:\n")
while user.upper() != "X":  
    if user.upper() == "E":
        x = input("Enter the message:\n")      
    if user.upper() == "V":
        if x != "":
            print("The message is:",x)
        else:
            print("The message is: no message yet")        
    if user.upper() == "L":
        print("List of files: 42.txt, 1015.txt")
    if user.upper() == "D":
        user1 = input("Enter the filename:\n")
        if user1 == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif user1 == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print ("Be happy")            
        else:
            print("File not found")
    print("Welcome to UCT BBS\n","MENU\n","(E)nter a message\n","(V)iew message\n","(L)ist files\n","(D)isplay file\n","e(X)it",sep = "")
    user = input("Enter your selection:\n")    
       
    
print("Goodbye!")