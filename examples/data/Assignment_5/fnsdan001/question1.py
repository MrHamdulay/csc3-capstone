import os
message = "no message yet"
cnt = 0

x = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n").upper()
while x!='X':
    if x == 'E':
        message = input("Enter the message: \n")
    elif x == 'V':
        print("The message is:", message)
    elif x == 'L':
        files = []
        for i in os.listdir():
            if i.count("txt"):
                
                files.append(i)
        print("List of files:", end = " ")
        print(", ".join(files[::-1]))
        

    elif x == 'D':
        try:
            
            filename = input("Enter the filename: \n")
            f = open(filename)
            lines = f.readlines()
            f.close()
            for i in lines:
                print (i[:len(i)-1])

        except:
            print("File not found")
    
            
       


    x = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n").upper()
            
            
if x == 'X':
    print("Goodbye!")
        
    
