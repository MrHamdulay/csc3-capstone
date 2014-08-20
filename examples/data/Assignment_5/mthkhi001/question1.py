#Khiraad Mathura
#MTHKHI001
#Assignment 5 Question 1

import sys
tempmessage ="no message yet"
newmessage = ""
choice = ""
while choice != "X" or choice != "x":    
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    choice = (input("Enter your selection:\n"))
    
    if(choice == "E" or choice == "e"):
        message = (input("Enter the message:\n"))
        newmessage = message
        
    if(choice == "V" or choice == "v"):
        if(newmessage == ""):
            print("The message is: " + tempmessage)
        else:
            print("The message is: " +newmessage)
        
    if(choice == "L" or choice == "l"):
        print("List of files: 42.txt, 1015.txt")
        
    if(choice == "D" or choice == "d"):
        filename = (input("Enter the filename:\n"))
        if(filename == "42.txt"):
            print("The meaning of life is blah blah blah ...")
           
        if (filename == "1015.txt"):
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            
        if(filename != "1015.txt" and filename != "42.txt"):
            print("File not found")
            
    if(choice == "X" or choice == "x"):
        print("Goodbye!")            
        sys.exit()
    
    



              