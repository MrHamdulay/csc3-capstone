# Simple BBS program simulation
# Badugela Mulisa
# 14 April 2014

def BBS():
       
    B=("Welcome to UCT BBS \nMENU \n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    E = ""

       
    while B: # loop so that the intro message which is defined as 'B' should always appear before user inputs something.
        print(B)
        S=input("Enter your selection:\n")
                      
        if S=='E' or S=='e':            
            E=input("Enter the message:\n")
        
        if S=='V' or S=='v':
            if E != "": # if v is inputed after a message 'E' is stored 
                print("The message is: "+E)
            else: # if v is inputed by user before message is stored
                print("The message is: no message yet")
                              
        if S=='L' or S=='l':
            print("List of files: 42.txt, 1015.txt")
        
        if S=='D' or S=='d':
            D=input("Enter the filename:\n")
            if D=='1015.txt':
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            elif D=='42.txt':
                print("The meaning of life is blah blah blah ...")
            elif D!='1015.txt' or D!='42.txt':
                print("File not found") # if text file inputed is anything other than 1015.txt and 42.tx
        if S=='X' or S=='x':
            print("Goodbye!")
            break # to stop the program when the user enters x
              
BBS()