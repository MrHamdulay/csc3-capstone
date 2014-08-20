"""simulating BBS
kennedy muranda
17/4/2014"""

#define the fuction
def BBS():
    s=""                    #making "string" an empty string
    message="no message yet"
    
    while s != "X" or s != "x": 
        #introductory message
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        
        #prompt user to select
        s=input("Enter your selection:\n")  
        
        #possible outcomes
        if s=="E" or s=="e":
            message=input("Enter the message:\n")   
            
        if s=="V" or s=="v":
            print("The message is:",message) 
            
        if s=="X" or s=="x":
            print("Goodbye!")                         
            break
        
        if s=="L" or s=="l":
            print("List of files: 42.txt, 1015.txt") 
            
        if s=="D" or s=="d":
            file_name=input("Enter the filename:\n") 
            if file_name=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file_name=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            
            else:
                print("File not found")

#call the function BBS             
BBS()                
                
        
        
    
