def start():
    
    print("Welcome to UCT BBS")
    
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    

    
            
    
    

User_Input = 'none so far'
message = "no message yet"

while User_Input != 'X' and User_Input!= 'x':
    start()
    User_Input = input("Enter your selection:\n")
    if  User_Input == 'E' or  User_Input == 'e':
        message = input("Enter the message: \n")
        
    elif  User_Input == 'V' or  User_Input == 'v':
        print("The message is:", message)
        
    elif  User_Input == 'L' or  User_Input == 'l':
        print("List of files: 42.txt, 1015.txt ")
        
    elif  User_Input == 'D' or  User_Input == 'd':
        y=input("Enter the filename: \n")
        if y =="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif y=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else: print("File not found")
        
print("Goodbye!")
            
        
     
    
    
