#Simulate a BBS
#Luke Schwartzkopff
#13 April 2014

menu = "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n"
message=""
file1,file2="The meaning of life is blah blah blah ...","Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"

ans=input(menu).upper()

while ans!="X":
    if ans=="E":
        message=input("Enter the message:\n")
        
    elif ans=="V":
        if(message!=""):
            print("The message is:",message)
        else: print("The message is: no message yet")
        
    elif ans=="L":
        print("List of files: 42.txt, 1015.txt")
        
    elif ans=="D":
        filen=input("Enter the filename:\n")
        if filen=="42.txt":
            print(file1)
        elif filen=="1015.txt":
            print(file2)
        else: print("File not found")
       
    ans=input(menu).upper()

print("Goodbye!")
            
        
        
        
        
            
        
    