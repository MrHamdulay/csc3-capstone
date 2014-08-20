""" program to simulate a simple BBS 
Thiloshni Moodley(MDLTHI019)
15 April 2014"""

#options given to user
print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")

message=''#stores message as an empty string
choice=input("Enter your selection:\n")

while choice.upper() != "X": #Below will happen unless the user types in x
    if choice.upper() == "E": #when the user choses option E
        message = input("Enter the message:\n")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")       
        choice=input("Enter your selection:\n")
        
    if choice.upper() =="V": #user choses option V
        if message == "" : #when no message stored
            print("The message is: no message yet")
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")       
            choice=input("Enter your selection:\n")            
        else:
            print("The message is:",message)
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")       
            choice=input("Enter your selection:\n")    
            
    if choice.upper() =="L": #user choses option L
            print("List of files: 42.txt, 1015.txt")
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")       
            choice=input("Enter your selection:\n")            
            
    if choice.upper() =="D": #user choses option D
            file_name = input("Enter the filename:\n")
            if file_name =="42.txt":
                print("The meaning of life is blah blah blah ...")
                print("Welcome to UCT BBS")
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")       
                choice=input("Enter your selection:\n")    
            elif file_name =="1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                print("Welcome to UCT BBS")
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")       
                choice=input("Enter your selection:\n")  
            else:
                print("File not found")
                print("Welcome to UCT BBS")
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")       
                choice=input("Enter your selection:\n")                
else: #when user types x
    print("Goodbye!")
    
                
                