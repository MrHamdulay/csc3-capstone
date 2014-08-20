#Question 1
#Kelly Goosen
#2014/04/16
bExit = False #Tells the loop when to stop
message = "no message yet"
while bExit == False:
    
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    selection=input("Enter your selection:\n") #Get selection from user

    if selection == 'E' or selection == 'e':
        message=input("Enter the message:\n")   
        
    elif selection == 'V' or selection == 'v':
        print ("The message is: " + message)
        
    elif selection == 'L' or selection == 'l':
        print("List of files: 42.txt, 1015.txt")
        
    elif selection == 'D' or selection == 'd':
        file=input("Enter the filename:\n")
        if file == '42.txt':
            print("The meaning of life is blah blah blah ...")    
        elif file == '1015.txt':
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")          
        else:
            print("File not found")          
            
    elif selection == 'X' or selection == 'x':
        bExit = True
        print("Goodbye!")
    
    