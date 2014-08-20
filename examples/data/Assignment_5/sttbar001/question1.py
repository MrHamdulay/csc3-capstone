# barak setton
# sttbar001 
# 17/04/14

message ="no message yet"
num =0
while num==0:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    c = input("Enter your selection: \n")
    c = str.upper(c)
    
    if c == 'E':
        message = input("Enter the message: \n")
        
    if c == 'V':
        print("The message is: "+message)
            
    if c== 'L':
        print("List of files: 42.txt, 1015.txt")
        
    if c== 'D':
        file = input("Enter the filename: \n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file =="1015.txt":
            print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy ")
        else:
            print("File not found")
            
    if c=="X":
        print("Goodbye!")
        num=1