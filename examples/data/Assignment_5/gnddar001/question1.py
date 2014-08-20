#Q1ASS4
#14.04.14
putin = ""
message = 1
while putin != "X" and putin != "x":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    putin = input("Enter your selection:\n")

    if putin == "E" or putin == "e":
        message = input("Enter the message:\n")
        
        
    if putin == "V" or putin == "v":
            
        if message != 1:
            print("The message is:" ,message)
            
        if message == 1:
            print("The message is: no message yet")            
        
    if putin == "l" or putin == "L":
        print("List of files: 42.txt, 1015.txt")
        
    if putin == "d" or putin == "D":
        newputin = input("Enter the filename:\n")
        
        if newputin == "42.txt":
            print("The meaning of life is blah blah blah ...")
            
        if newputin == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            
        if newputin != "42.txt" and newputin != "1015.txt":
            print("File not found")
            
    if putin == "X" or putin == "x":
        print("Goodbye!")
    
    