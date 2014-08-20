"""Menu:User input Question 1
Assignment 5 
Nandani Birjanund
16/04/14"""

print("Welcome to UCT BBS") #Menu listed 
print("MENU")

print("(E)nter a message") #E or e
print("(V)iew message") #V or v
print("(L)ist files") #L or l
print("(D)isplay file") #D or d
print("e(X)it ") #X or x (ends program)  

selection = input("Enter your selection: \n")   #User inputs a selection

txtMessage = ""
while selection:  
            if selection == 'E' or selection == 'e':       #Menu E or e selection 

                        txtMessage = input("Enter the message:\n")
                        s = ""
    
            if selection == 'V' or selection == 'v':       #Menu V or v selection
                        if txtMessage == "":
                                    print("The message is: no message yet")                        
                        else:
                                    print("The message is:",txtMessage) 
                                    s = ""
                                    
            if selection == 'L' or selection == 'l':  #Menu L or l selection
                        print("List of files: 42.txt, 1015.txt")
                        s =""
            
            if selection == 'D' or selection == 'd':     #Menu D or d selection
                        fileName = input("Enter the filename: \n") #To select one of the files (1015.txt or 42.txt)
                        
                        if fileName == "42.txt" or fileName == '1015.txt':
                                    if fileName == '42.txt':
                                                print("The meaning of life is blah blah blah ...") #For 42.txt
                                    
                                    elif fileName == '1015.txt':
                                                print("Computer Science class notes ... simplified") #For 1015.txt
                                                print("Do all work")
                                                print("Pass course")
                                                print("Be happy")
        
                        else:
                                    print("File not found") # When user inputs anything other than 1015.txt or 42.txt
                        selection=""
          
            if selection == 'X' or selection == 'x':     #Menu X or x selection
                        print("Goodbye!") 
                        s=""
                        break
            
            print("Welcome to UCT BBS")         #Menu is printed 
            print("MENU")
                        
            print("(E)nter a message")  #Enters the message and other lines of menu
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it ") #Exits loop
                        
            selection = input("Enter your selection:\n") #User inputs a selection
else:
            print("Welcome to UCT BBS")     #Prints welcome page
            print("MENU")
                                    
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it ") #Exits loop
                                    
            selection = input("Enter your selection:\n") #User inputs a selection       