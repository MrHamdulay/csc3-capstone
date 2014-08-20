#Taahirah achmat
#ACHTAA001
#program to stimulate BBS

insert = ""   #empty string, the loop condition can be true and can begin
typetext = 1

#entering print statements that make up BBS
while insert != "X" and insert != "x":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    insert = input("Enter your selection:\n")

#introducing conditions
    if insert == "E" :
        typetext = input("Enter the message:\n")
        
    if insert == "e" :
        typetext = input("Enter the message:\n")
        
    if insert == "V" or insert == "v":
             
        if typetext != 1:
            print("The message is:" ,message)
            
        if typetext == 1:
            print("The message is: no message yet")            
         
    if insert == "l" or insert == "L":
        print("List of files: 42.txt, 1015.txt")
        
    if insert == "d" :
        insert2 = input("Enter the filename:\n")
         
    if insert == "D":   
        insert2 = input("Enter the filename:\n")
        
        if insert2 == "42.txt":
            print("The meaning of life is blah blah blah ...")
             
        if insert2 == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            
        if insert2 != "42.txt" :
            print("File not found")
            
        if insert2 != "1015.txt":   
            print("File not found")
             
    if insert == "X" :
        print("Goodbye!")