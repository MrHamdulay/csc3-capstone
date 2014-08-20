#program to perform text-based messages
#vuyolwethu nkosi
#14 april 2014

def text_message(): #program definition
    #print menu
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selc = input("Enter your selection:\n") #get input
    lc = selc.lower() #change to lower case for later insertions
    file_1 = "42.txt" #file names
    file_2 = "1015.txt"
    while lc!="python": #creating while loop to check for test cases
            if lc=="x": #checking first selection
                    print("Goodbye!")
                    break #end program
            elif lc=="e": 
                e_message = input("Enter the message:\n") #user puts in input
                print("Welcome to UCT BBS") #must print menu again each tim
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")               
                selc = input("Enter your selection:\n")
                lc = selc.lower()
                if lc=="v": 
                        print("The message is:",e_message) #recalling message put in before by user
                        print("Welcome to UCT BBS")
                        print("MENU")
                        print("(E)nter a message")
                        print("(V)iew message")
                        print("(L)ist files")
                        print("(D)isplay file")
                        print("e(X)it")                        
                        selc = input("Enter your selection:\n")
                        lc = selc.lower()                
                        continue #program must skip and go to next portion of program                       
                continue
            elif lc=="v":
                if lc=="v" and lc!="e": #if no message inputed yet
                        print("The message is: no message yet")
                        print("Welcome to UCT BBS")
                        print("MENU")
                        print("(E)nter a message")
                        print("(V)iew message")
                        print("(L)ist files")
                        print("(D)isplay file")
                        print("e(X)it")                        
                        selc = input("Enter your selection:\n")
                        lc = selc.lower()                
                        continue
               
            elif lc=="l":
                print("List of files: ",file_1,","," ", file_2,sep="") #list files
                print("Welcome to UCT BBS")
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")                
                selc = input("Enter your selection:\n")
                lc = selc.lower()
                if lc=="v":
                        print("The message is:",e_message)
                        print("Welcome to UCT BBS")
                        print("MENU")
                        print("(E)nter a message")
                        print("(V)iew message")
                        print("(L)ist files")
                        print("(D)isplay file")
                        print("e(X)it")                       
                        selc = input("Enter your selection:\n")
                        lc = selc.lower()                
                        continue 
                continue  
            elif lc=="d":
                file_nm = input("Enter the filename:\n") #requiring input from user

                if file_nm==file_1:
                        print("The meaning of life is blah blah blah ...")
                        print("Welcome to UCT BBS")
                        print("MENU")
                        print("(E)nter a message")
                        print("(V)iew message")
                        print("(L)ist files")
                        print("(D)isplay file")
                        print("e(X)it")                        
                        selc = input("Enter your selection:\n")
                        lc = selc.lower()                        
                        continue
                elif file_nm==file_2:
                        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                        print("Welcome to UCT BBS")
                        print("MENU")
                        print("(E)nter a message")
                        print("(V)iew message")
                        print("(L)ist files")
                        print("(D)isplay file")
                        print("e(X)it")                        
                        selc = input("Enter your selection:\n")
                        lc = selc.lower()                        
                        continue
                elif file_nm!=file_1 or file_nm!=file_2: #if file user is not defined, print file not found
                        print("File not found")
                        print("Welcome to UCT BBS")
                        print("MENU")
                        print("(E)nter a message")
                        print("(V)iew message")
                        print("(L)ist files")
                        print("(D)isplay file")
                        print("e(X)it")                        
                        selc = input("Enter your selection:\n")
                        lc = selc.lower()                        
                        continue  #program should continue until user inputs x
text_message()
                
                
    
   
   
            
            
        
    
    