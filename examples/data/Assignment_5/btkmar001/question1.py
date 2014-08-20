# Assignment 5, Question 1
# A program that simulates a simple BSS
# Martin Batek
# 14 April 2014

answer = ""
message = "no message yet"
# Output if no message has been saved
files = ["42.txt","1015.txt"]
# Names of files
acceptable = ["E","V","L","D","X"]
# Acceptable selections from main menu

while answer != "X":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    answer = input("Enter your selection:\n")
    
    answer = answer.upper()
    
    if answer == "E":
        message = input("Enter the message:\n")
        
    elif answer == "V":
        print("The message is:",message)
        
    elif answer == "L":
        print("List of files:", ", ".join(files))
    
    elif answer == "D":
        filename = input("Enter the filename:\n")
        if filename == files[0]:
            print("The meaning of life is blah blah blah ...")
            
        elif filename == files[1]:
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            
        else:
            print("File not found")
            
    elif answer not in acceptable:
        print("Invalid answer. Please enter a valid one.")
            
print("Goodbye!")
            
            
            