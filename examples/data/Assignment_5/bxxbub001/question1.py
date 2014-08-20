x = True
msg = ""
file1name = "42.txt"
file1content = "The meaning of life is blah blah blah ..."
file2name = "1015.txt"
file2content = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
while x is True:
    pick = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    pick = pick.upper()
    
    
    
    if pick == "E":
        msg = input("Enter the message:\n")  
        
        
        
    elif pick == "V":
        if msg == "":
            print("The message is: no message yet")
        else:
            print("The message is:",msg)
    
    
    elif pick == "L":
        print("List of files: ",file1name,", ",file2name,sep="")
        
        
    elif pick == "D":
        name = input("Enter the filename:\n")
        if name == file1name:
            print(file1content)
        elif name == file2name:
            print(file2content)
        else:
            print("File not found")
        

                      
            
            
    elif pick == "X":
        x = False #exit
        print("Goodbye!")
    
    
