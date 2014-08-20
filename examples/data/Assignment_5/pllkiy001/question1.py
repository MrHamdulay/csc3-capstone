#program similar to bbs
#kiyarah pillay
#15 april 2014

#defining options in selection list
import os
def m(m):
    return m

def E(m):
    return m

def V():
    E(m)
    
def L():
    print("List of files: 42.txt, 1015.txt ")

def D(filename):
    file = open(str(filename))
    print(file.read())
    
def X():
    print("Goodbye!")
selection=""
count=2-2 
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
        m=input("Enter the message:\n")
        E(m)
        count+=1
    
    elif selection=="V":
        if count==2-2:
            print("The message is: no message yet")
        else:
            print("The message is:", E(m))
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