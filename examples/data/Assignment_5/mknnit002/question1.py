#nitisha makanjee
#16 april 2014
#bulletin board systems


import os.path
message="no message yet"

#Build the menu
def openmenu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")  
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

#Execute selection
openmenu()
select=input("Enter your selection:""\n")

if select.upper()=="E":
    message=input("Enter the message:""\n")
    openmenu()
    select=input("Enter your selection:""\n")

if select.upper()=="V":
    print("The message is:", message)
    openmenu()
    select=input("Enter your selection:""\n")
    
if select.upper()=="L":
    if os.path.isfile("42.txt") and os.path.isfile("1015.txt"):
        print("List of files: 42.txt, 1015.txt")
    else:
        print("File not found")
    openmenu()
    select=input("Enter your selection:""\n")  
    
if select.upper()=="D":
    fname=input("Enter the filename:""\n")
    if fname=="42.txt":
        file=open(fname)
        for line in file:
            print(line)
    elif fname=="1015.txt":
        file=open(fname)
        for line in file:
            print(line)
    else:
        print("File not found")
    openmenu()
    select=input("Enter your selection:""\n") 

if select.upper()=="X":
    print("Goodbye!")