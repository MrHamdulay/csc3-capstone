"""Michelle Lu
12 April 2014"""

def menu():    #create a function for menu
    print("Welcome to UCT BBS")
    print("MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    
menu() 
answer=input("Enter your selection:\n")
message="no message yet" #prints no message yet until they have entered one.
while answer!="": #while they haven't entered an empty string
    if answer=="E" or answer=="e":
        message=input("Enter the message:\n") #assigns the message variable
        menu()
        answer=input("Enter your selection:\n")   
        
              
    elif answer=="V" or answer=="v":
        print("The message is:", message)
        menu()
        answer=input("Enter your selection:\n")   
        
              
    elif answer=="L" or answer=="l":
        print("List of files: 42.txt, 1015.txt")
        menu()
        answer=input("Enter your selection:\n")   
        
              
    elif answer=="D" or answer=="d":
        file=input("Enter the filename:\n")
        if file=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
        menu()
        answer=input("Enter your selection:\n")   
           
                  
    elif answer=="X" or answer=="x":
        print("Goodbye!")
        answer="" #empty string breaks the loop
   
    
