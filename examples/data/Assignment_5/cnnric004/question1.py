d42 = "The meaning of life is blah blah blah ..."
d1015 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
selection = ""
message = "no message yet"
while(selection.upper != "X"):
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    selection = input("Enter your selection:\n")
    
    if(selection.upper() == "E"):
        message = input("Enter the message:\n")
    if(selection.upper() == "V"):
        print("The message is:",message)
        
    if(selection.upper() == "L"):
        print("List of files: 42.txt, 1015.txt")
        
    if(selection.upper() == "D"):
        fileName = input("Enter the filename:\n")
        
        if(fileName == "42.txt"):
            print(d42)
        elif(fileName == "1015.txt"):
            print(d1015)
        else:
            print("File not found")
            
    if(selection.upper() == "X"):
        break
            
            
print("Goodbye!")
    
           