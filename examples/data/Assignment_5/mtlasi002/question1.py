#Asil Motala
#13 April 2014
#Assignment 5
#Question 1

message="no message yet"
one="The meaning of life is blah blah blah ..."
two="Computer Science class notes ... simplified"+"\nDo all work"+"\nPass course"+"\nBe happy"
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    select=input("Enter your selection:\n")
    selection=select.upper()
    
    if selection=="E":
        message=input("Enter the message:\n")
    
    elif selection=="V":
        print("The message is:",message)
    
    elif selection=="L":
        print("List of files: 42.txt, 1015.txt")
    
    elif selection=="D":
        file=input("Enter the filename:\n")
        if file=="42.txt":
            print(one)
        elif file=="1015.txt":
            print(two)            
        else:
            print("File not found")
    
    elif selection=="X":
        print("Goodbye!")
        break