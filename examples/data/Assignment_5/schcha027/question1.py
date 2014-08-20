opt="w"
message="no message yet"

import os

while opt!="x":
    print("Welcome to UCT BBS",)
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    opt=input("Enter your selection:\n")
    
    
    
    if opt=="e":
        message=input("Enter the message:\n")
    elif opt=="v":
        print("The message is: ",message,sep="")
    elif opt=="l":
        filelist=""
        i =0
        for file in os.listdir():
            if file.endswith(".txt"):
                filelist=file+", "+filelist                
        length=len(filelist)-2
        print("List of files: ", filelist[0:length],sep="")
        
    elif opt=="d":
        filename=input("Enter the filename:\n")     
        if(filename=="42.txt"):
            print("The meaning of life is blah blah blah ...")
        elif(filename=="1015.txt"):
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
            
        
    else:
        print("Goodbye!")
