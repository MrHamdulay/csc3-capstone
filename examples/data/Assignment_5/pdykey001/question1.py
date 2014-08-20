"""Uct BBS program
Keyoolin Padayachee
16 April 2014
"""
#Creating of the 2 files
file=["42.txt","1015.txt"]
fileRef=["The meaning of life is blah blah blah ...","Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"]
selection=""
message=""
while selection!="X":
    #display the menu when selection is not exit
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection=input("Enter your selection:\n").upper()
    if selection == "X":
        print("Goodbye!")
        break
    elif selection == "E": message=input("Enter the message:\n")
    elif selection == "V":
        if message=="" : print("The message is: no message yet")
        else : print("The message is:",message)
    elif selection == "L": print("List of files: "+file[0],file[1],sep=", ")
    elif selection == "D":
        fileSelect=input("Enter the filename:\n")
        if fileSelect in file:
            print(fileRef[file.index(fileSelect)])
        else: print("File not found")
        
        
    
    
    
