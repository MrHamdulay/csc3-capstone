#Assignment 5 - Question 1
#Aidan de Nobrega
#13/04/2014

message = "no message yet" #default message

def uctBBS(): #Home menu 7-15
    '''UCT BUlletin Board System'''
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    select = input("Enter your selection:\n") #User's menu choice
    
    if select == "E" or select == "e":
        global message #To change message globally
        message = input("Enter the message:\n")
        uctBBS() #Return to home menu
        
    elif select == "V" or select == "v":
        print ("The message is: " + message)
        uctBBS()
        
    elif select == "L" or select == "l":
        print("List of files: 42.txt, 1015.txt")
        uctBBS()
        
    elif select == "D" or select == "d":
        file_select = input("Enter the filename:\n")
        
        if file_select == "42.txt":
            print("The meaning of life is blah blah blah ...")
            uctBBS()
        elif file_select == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            uctBBS()
        else:
            print ("File not found")
            uctBBS()
            
    elif select == "X" or select == "x":
        print ("Goodbye!")

uctBBS()