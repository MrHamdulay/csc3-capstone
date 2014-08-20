print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")
x=input("Enter your selection:\n")
s="no message yet"
E=""
file1="42.txt"
file2="1015.txt"
content1="The meaning of life is blah blah blah ..."
content2="Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy"
while(x!="X" and x!="x"):
    if (x=='E' or x=="e"):
        E=input("Enter the message:\n")
        s=E
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        x=input("Enter your selection:\n")
    if(x=="V" or x=="v"):
        
        print("The message is:",s)
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        x=input("Enter your selection:\n")
    if(x=="L" or x=="l"): 
              
            
        print("List of files: 42.txt, 1015.txt")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        x=input("Enter your selection:\n")    
    if(x=="D" or x=="d"):
        f=input("Enter the filename:\n")
        if(f==file1):
            print(content1)
        elif(f==file2):
            print(content2)
        else:
            print("File not found")
                

        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        x=input("Enter your selection:\n")
print("Goodbye!")