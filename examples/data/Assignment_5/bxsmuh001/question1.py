#Assignment 5, Question 1
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 16/04/2014

#This program is designed to simulate a simple BBS.

#Defining the function BBS() to simulate the BBS.
def BBS():
    selections = ["e","E","v","V","l","L","d","D","x","X"]
    filesList = ["42.txt","1015.txt"]
    storedMessage = ""
    while(str(selections) != "x" or str(selections) != "X"):    
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        
        userSelection = input("Enter your selection:\n")
        
        
        if(userSelection == selections[0] or userSelection == selections[1]):
            userMessage = input("Enter the message:\n")
            storedMessage = userMessage
            
        if(userSelection == selections[2] or userSelection == selections[3]):
            if(storedMessage != "" ):
                print("The message is:", storedMessage)
                
            else:
                print("The message is: no message yet")
                continue
           
        if(userSelection == selections[4] or userSelection == selections[5]):
            print("List of files:", filesList[0]+",", filesList[1])
            
        if(userSelection == selections[6] or userSelection == selections[7]):
            fileName = input("Enter the filename:\n")
            if(fileName == filesList[0]):
                print("The meaning of life is blah blah blah ...")
            elif(fileName == filesList[1]):
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")  
                print("Be happy")    
            else:
                print("File not found")
            
       
        if((str(userSelection) == selections[8]) or (str(userSelection) == selections[9])):
            break
        
    print("Goodbye!")

BBS()