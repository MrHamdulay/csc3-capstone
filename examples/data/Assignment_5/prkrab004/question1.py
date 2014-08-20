#Assignment 5
#Question 1
#Rabia Parker
#Due Date:17/04/14

def UCT_BBS():
    start=""
    message=''
    while start !='X' or start !='x':
        print("Welcome to UCT BBS")
        print("MENU")          #iterations
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        S=input("Enter your selection:\n") #save selection
        #Enter message
        if S =='E' or S == 'e' :
            new_message=input("Enter the message:\n")
            message+=new_message
        #View Selection
        elif S == 'V' or S=='v':
            if message !='':
                print("The message is:", message)
            else:
                print("The message is: no message yet")
        #List files
        elif S=='L' or S=='l':
            print("List of files: 42.txt, 1015.txt")
        #Display file
        elif S=='D' or S=='d':
            F=input("Enter the filename:\n")
            if F=='42.txt':
                print("The meaning of life is blah blah blah ...")
            elif F=='1015.txt':
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print("File not found")
        #Exit
        else:
            print("Goodbye!")
            break
        start+=S
        
UCT_BBS()
    
            
            
            
        
        
        
        
        