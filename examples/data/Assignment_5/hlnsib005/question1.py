"""Sibulele Hlongwane
Date: 15 April
Question 1
BBS Simulation"""

smessage=""
icount=1
while icount>0:
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    sinput= input("Enter your selection:\n")
    #Checks user selection 
    if sinput.upper()== "E":
        smessage= input("Enter the message:\n")
     #Checks whether there is a message?   
    if sinput.upper()== "V":
        if smessage=="":
            print("The message is: no message yet")
        else:
                print("The message is:",smessage)
      #Textfiles          
    if sinput.upper()== "L":     
        print("List of files: 42.txt, 1015.txt")
    if sinput.upper()== "D":
        sfile= input("Enter the filename:\n")
        if (sfile!="42.txt") and (sfile!="1015.txt"):
            print("File not found")
        if sfile== "42.txt":
            print("The meaning of life is blah blah blah ...")
        if sfile=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
    #Exits
    if sinput.upper()== "X":
        print("Goodbye!")
        icount=0
        
