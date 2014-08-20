"""question1: program to produce menu
thrianka naidoo
ndxthr005"""

print("Welcome to UCT BBS")                     #List options - Menu
print("MENU")

print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it ")

selection = input("Enter your selection: \n")   #Input for user
s = selection.upper()
txtMessage = ""
while s:  
            if s == 'E':                        #Menu selection 1 

                        txtMessage = input("Enter the message:\n")
                        s = ""
    
            if s == 'V':                        #Menu selection 2
                        if txtMessage == "":
                                    print("The message is: no message yet")                        
                        else:
                                    print("The message is:",txtMessage)
                                    s = ""
                                    
            if s == 'L':                        #Menu selection 3
                        print("List of files: 42.txt, 1015.txt")
                        s =""
            
            if s == 'D':                        #Menu selection 4 
                        fileName = input("Enter the filename: \n")
                        
                        if fileName == "42.txt" or fileName == '1015.txt':
                                    if fileName == '42.txt':
                                                print("The meaning of life is blah blah blah ...")
                                    
                                    if fileName == '1015.txt':
                                                print("Computer Science class notes ... simplified")
                                                print("Do all work")
                                                print("Pass course")
                                                print("Be happy")
        
                        else:
                                    print("File not found")
                        s=""
          
            if s == 'X':                        #Menu selection 5
                        print("Goodbye!") 
                        s=""
                        break
            
            print("Welcome to UCT BBS")         #List options - Menu
            print("MENU")
                        
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it ")
                        
            selection = input("Enter your selection:\n") #Input for user
            s = selection.upper()
else:
            print("Welcome to UCT BBS")         #List options - Menu
            print("MENU")
                                    
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it ")
                                    
            selection = input("Enter your selection:\n") #Input for user
            s = selection.upper()        