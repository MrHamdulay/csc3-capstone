'''A program that simulates a simple BBS
Sanele Mdlalose
13-04-2014
Assignment5,Question1'''

def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

mssg="no message yet"
while mssg:    
    menu()
    main_prompt=input("Enter your selection:\n")
    if main_prompt=="E" or main_prompt=="e":
        mssg_prompt=input("Enter the message:\n")
        mssg=mssg_prompt
        continue
    
    elif main_prompt=="V" or main_prompt=="v":
        print("The message is:",mssg)
        
    
    elif main_prompt=="L" or main_prompt=="l":
        print("List of files: 42.txt, 1015.txt")
        
    elif main_prompt=="D" or main_prompt=="d":
        filename_prompt=input("Enter the filename:\n")
        if filename_prompt=="42.txt":
            print("The meaning of life is blah blah blah ...")
         
        elif filename_prompt=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            
        else:
            print("File not found")
    
    elif main_prompt=="X" or main_prompt=="x":
        print("Goodbye!")
        break
    
        