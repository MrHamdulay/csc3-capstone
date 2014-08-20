selection = 0
message = 0

while selection!="X":
        print ("Welcome to UCT BBS")
        print ("MENU")
        print ("(E)nter a message") #4 functions for users: Enter a message, View message, List files, Display files
        print ("(V)iew message")
        print ("(L)ist files")
        print ("(D)isplay file")
        print ("e(X)it")
        selection = input ("Enter your selection: \n")
        selection = selection.upper()
        
        if selection == "E":
                message = input("Enter the message: \n")
        
        elif selection == "V":
                if message == 0:
                        print ("The message is: no message yet")
                else:
                        print ("The message is:",message)
       
        elif selection == "L": #2 files are 42.txt and 1015.txt
                print ("List of files: 42.txt, 1015.txt")
                      
        elif selection == "D":
                filename = input ("Enter the filename: \n") #if input = d: program is asking for either 42.txt or 1015.txt
                
                if filename == "42.txt": #42.txt = The meaning of life is blah blah blah ...
                        print ("The meaning of life is blah blah blah ...")
                
                elif filename == "1015.txt": #1015.txt = Computer Science class notes .../ Do all work/ Pass course/ Be happy
                        print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                
                else:
                        print ("File not found")
print ("Goodbye!") #User can exit using input of X


