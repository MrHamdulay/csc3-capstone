# question1.py
# camilla craven
# program to simulate a simple BBS with one stored message and 2 fixed files
# 14 April 2014


# printing welcome
print("Welcome to UCT BBS")
print("MENU")

# printing options
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")

# user inputs choice
Q = input("Enter your selection:\n")


# setting continuous loop until user exits using "X"
while Q != "X" and Q != "x":
    
    if Q == "E" or Q == "e": # if user inputs "E"
        E = input("Enter the message:\n") # user will be prompted to input message
        
        # prints welcome and options again
        print("Welcome to UCT BBS")
        print("MENU")
        
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it") 
        
        # again user is asked to input choice
        Q = input("Enter your selection:\n")
       
        
    elif Q == "V" or Q == "v": # if user enters "V"
        try:
            print("The message is:", E) # prints the last message the user has entered
            
        except NameError:
            print("The message is: no message yet") # if E does not exist and error occurs
            
               
        # welcome and options
        print("Welcome to UCT BBS")
        print("MENU")
        
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it") 
        
        # user prompted for new selection
        Q = input("Enter your selection:\n")       
        
        
    elif Q == "L" or Q == "l": # if user chooses "L"
        print("List of files: 42.txt, 1015.txt") # informs user of available files

        # welcome and options
        print("Welcome to UCT BBS")
        print("MENU")
        
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it") 
        
        # user prompted for new selection
        Q = input("Enter your selection:\n") 
        
    
    elif Q == "D" or Q == "d": # if user selects "D"
        file = input("Enter the filename:\n") # user prompted to enter name of desired file
        
        if file == "42.txt": # if user enters "42.txt"
            # prints file
            print("The meaning of life is blah blah blah ...")
            
            # welcome and options
            print("Welcome to UCT BBS")
            print("MENU")
            
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it") 
            
            # user prompted to enter new selection
            Q = input("Enter your selection:\n")             
            
        elif file == "1015.txt": # if user inputs file name "1015.txt"
            # prints message in file
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            
            # welcome and options
            print("Welcome to UCT BBS")
            print("MENU")
            
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it") 
            
            # user once again prompted for choice
            Q = input("Enter your selection:\n")             
            
        else: # if user inputs a file that does not appear on the list given (that does not exist)
            print("File not found") # informs user that file is not a viable option
            
            # welcome and options
            print("Welcome to UCT BBS")
            print("MENU")
            
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it") 
            
            # prompts user for selection
            Q = input("Enter your selection:\n")         



if Q == "X" or Q == "x": # if user inputs "X"
    print("Goodbye!") # prints goodbye (informs user program is finished)
    # exits while loop and program finishes