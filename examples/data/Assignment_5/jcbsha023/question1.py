#programe to simulate simple Bulletin Board System(BBS)
#Anthony Jacob
#13-04-14

def BBS():
    string=""                    #making "string" an empty string
    message="no message yet"
    
    while string != "X" or string != "x": 
        #INTRODUCTION        
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        
        string=input("Enter your selection:\n")  #asking user to enter a selection
        
        #series of if statements to give respective outputs
        if string=="E" or string=="e":
            message=input("Enter the message:\n")     #if user select E
        if string=="V" or string=="v":
            print("The message is:",message)          #if user selects v
        if string=="X" or string=="x":
            print("Goodbye!")                         #if user selects x
            break
        if string=="L" or string=="l":
            print("List of files: 42.txt, 1015.txt")  #if user selects l
        if string=="D" or string=="d":
            file_name=input("Enter the filename:\n") #if user selects d
            if file_name=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file_name=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            
            else:
                print("File not found")
               
BBS()                #calling the function BBS
                
        
        
    
