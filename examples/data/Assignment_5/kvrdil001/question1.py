#UCT BBS assignment
#Dilan Koovarjee
#15 April 2014
x = " "
message= "no message yet"
while x: 
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    x=input("Enter your selection:\n")
    if x== "e" or x =="E":
        message=input("Enter the message:\n")
    if x== "v" or x=="V":
        print("The message is:",message)
    if x== "l" or x== "L":
        print("List of files: 42.txt, 1015.txt")
    if x== "d" or x== "D":
        file=input("Enter the filename:\n")
        if file== "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        elif file != "42.txt" or file!= "1015.txt":
            print("File not found")
    if x== "x" or x== "X":
        print("Goodbye!")
        break
        

    
        

            
    
        
        
        
        
 