"""BBS simulation
danica van der zandt
14 april 2014"""

select=""
vv=""



#print the welcome and menu after every display
while select!="X": 
        #DISPLAY WELCOME AND MENU
        print("Welcome to UCT BBS")
        print("MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        select=input("Enter your selection:\n")    
##the above never goes into the code below, it just prints the menu over and over again##    
    
#if the user wants to enter a message
        if select=="E" or  select =="e":
                vv=input("Enter the message:\n")
                
                
      
    
#if the user wants to view a previously entered message
        #if string is empty print no message yet
        elif select == "V" or select=="v":
                if vv=="":
                        print("The message is: no message yet")
                else:
                        print("The message is:",vv)
    
#if the user wants list all saved files
        elif select == "L" or select =="l":
                print("List of files: 42.txt, 1015.txt")
    
#if a user wants to open a specific file
  #files must be listed
  #if not listed print file not found
        elif select == "D" or select =="d":
                file=input("Enter the filename:\n")
                if file== "42.txt":
                        print("The meaning of life is blah blah blah ...")
                elif file== "1015.txt":
                        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                else:
                        print("File not found")

  
#if the user wants to exit    
        elif select=="X" or  select =="x":
                print("Goodbye!")
                break


