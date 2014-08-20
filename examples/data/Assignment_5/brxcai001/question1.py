#Program to stimulate simple BBS with one stored message and two fixed files.
#BRXCAI001
#16 April 2014

#defining main function.
def uctbbs():
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
uctbbs()

#user must select option avaibale, convert a lower option to an upper case.
sel = input("Enter your selection:\n")
selectionU = sel.upper()
message=''

#carry out instructions according to option previously selected, using a break loop if exit option is selected.
if selectionU == "X":
    print("Goodbye!")
while selectionU != "X":
    while selectionU == "E":
        message = input("Enter the message:\n")
        uctbbs()
        sel = input("Enter your selection:\n")
        selectionU = sel.upper()
        if selectionU == "X":
            print("Goodbye!")
        break
    while selectionU == "V":
        if message == "":
            print("The message is:","no message yet")
        else:
            print("The message is:",message)
        uctbbs()
        sel = input("Enter the message:\n")
        selectionU = sel.upper()
        if selectionU == "X":
            print("Goodbye!")
        break 
    while selectionU == "L":
        print("List of files:","42.txt, 1015.txt")
        uctbbs()
        sel = input("Enter your selection:\n")
        selectionU = sel.upper() 
        if selectionU == "X":
            print("Goodbye!")
        break
    while selectionU == "D":
        filename = input("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
            uctbbs()
            sel = input("Enter your selection:\n")
            selectionU = sel.upper() 
            if selectionU == "X":
                print("Goodbye!")
            break  
        if filename == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            uctbbs()
            sel = input("Enter your selection:\n")
            selectionU = sel.upper() 
            if selectionU == "X":
                print("Goodbye!")
            break     
        else:
            print("File not found")
            uctbbs()
            sel = input("Enter your selection:\n")
            selectionU = sel.upper() 
            if selectionU == "X":
                print("Goodbye!")
            break
        break
            
    
        
        
        

        
    
    
            
            
            
            
    
        
    
