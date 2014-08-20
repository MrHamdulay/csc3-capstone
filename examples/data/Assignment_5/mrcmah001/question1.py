a="42.txt" 
b="1015.txt" #assign variable to files
x=""
y="no message yet"
while x != "x" or x != "X":
    print("Welcome to UCT BBS") #main menu. to be repeated while the 
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    x=input("Enter your selection:\n")
    if x == "E" or x== "e":
        y=input("Enter the message:\n") #storemessage
    if x == "V" or x=="v":
        print("The message is:", y) #used y to display message 
        
    if x== "L" or x == "l":
        print("List of files: 42.txt, 1015.txt")
        
    if x=="D" or x=="d":
        d=input("Enter the filename:\n")
        if d==a:
            print("The meaning of life is blah blah blah ...")
        elif d==b: #use a and b to determine what text is displayed
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else :print("File not found")
    if x=="X" or x=="x":
        print("Goodbye!")
        break #end loop
    

    
        
    
    
    
  