""" program to mimic a bbs interface
    kevin kumasamba
    14 april 2014"""

import os
# returning the message
def message(message):
    return message
    
# entering a message that must be stored
# message=input("Enter a message:\n")
def E(message):
    return message

# returning that message when asked for it     
def V():
    E(message)

# listing available files
def L():
    print("List of files: 42.txt, 1015.txt ")

# displaying files
# filename=input("Enter the filename:\n")
def D(filename):
    file = open(str(filename))
    print(file.read())

# exiting 
def X():
    print("Goodbye!")

# allowing selection
selection=""
count=0 # easy fix to control the no message yet dilemma
while selection!="X":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection=input("Enter your selection:\n").upper()
  
    if selection=="E":
        message=input("Enter the message:\n")
        E(message)
        count+=1
    
    elif selection=="V":
        if count==0:
            print("The message is: no message yet")
        else:
            print("The message is:", E(message))
    elif selection=="L":
        L()
    elif selection=="D":
        filename=input("Enter the filename:\n")
        if os.path.isfile(filename): 
            D(filename)
        else:
            print("File not found")
    elif selection=="X":
        X()
        
            
    
    
    
    

    
    