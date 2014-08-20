print("Welcome to UCT BBS", "MENU", "(E)nter a message", "(V)iew message", "(L)ist files", "(D)isplay file", "e(X)it", sep='\n')
c=input("Enter your selection:\n")

message=("no message yet")

while c!=("x") and c!=("X"):
    
    if c==("E") or c==("e"):
        message=input("Enter the message:\n")
        print("Welcome to UCT BBS", "MENU", "(E)nter a message", "(V)iew message", "(L)ist files", "(D)isplay file", "e(X)it", sep='\n')
        c=input("Enter your selection:\n")
        
    if c==("V") or c==("v"):
        print(message)
        print("Welcome to UCT BBS", "MENU", "(E)nter a message", "(V)iew message", "(L)ist files", "(D)isplay file", "e(X)it", sep='\n')
        c=input("Enter your selection:\n")
        
    if c==("L") or c==("l"):
        print("List of files: 42.txt, 1015.txt")
        print("Welcome to UCT BBS", "MENU", "(E)nter a message", "(V)iew message", "(L)ist files", "(D)isplay file", "e(X)it", sep='\n')
        c=input("Enter your selection:\n")        
    
    if c==("D") or c==("d"):
        file=input("Enter the filename:\n")
        
        if file==("42.txt"):
            print("The meaning of life is blah blah blah ...")
            
        elif file==("1015.txt"):
            print("Computer Science class notes ... simplified", "Do all work", "Pass course", "Be happy", sep='\n')
            
        else:
            print("File not found")
            
        print("Welcome to UCT BBS", "MENU", "(E)nter a message", "(V)iew message", "(L)ist files", "(D)isplay file", "e(X)it", sep='\n')
        c=input("Enter your selection:\n")                
        

if c==("x") or c==("X"):
    print("Goodbye!")