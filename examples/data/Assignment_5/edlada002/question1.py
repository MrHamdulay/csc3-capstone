""" Bulletin Board Systems program
Adam Edelberg
15 April 2014"""

selection = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")

fileList=["42.txt", "1015.txt"]
fileContent = ["The meaning of life is blah blah blah ...","Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"]
message = "no message yet"
  

while True:
    
    if (selection.upper() == "X"):
        print("Goodbye!")
        break
    
    elif (selection.upper() == "E"):
        message = input("Enter the message:\n")
        
        selection = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    
    elif (selection.upper() == "V"):
        
        print ("The message is:" , message)
        selection = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    
    elif (selection.upper() == "L"):
        
        print("List of files: 42.txt, 1015.txt")
        selection = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
        
        
    elif (selection.upper() == "D"):
        fileName = input("Enter the filename:\n")
        
        for i in range (len(fileList)):
            if (fileList[i]==fileName):
                print (fileContent[i])
                break
                
        else:
            print("File not found")
            
        selection = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")        

        
   
        

    
    