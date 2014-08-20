print("Welcome to UCT BBS\nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")

choice=input("Enter your selection: \n")
choice=choice.upper()
message=''

if choice=='X' :
    print("Goodbye!")
if choice=='E' :
        message=input("Enter the message: \n")
if choice=='V':
    if message=='':
        print("The message is: no message yet")
    else:
        print("The message is:")    
if choice=='L':
        print("List of files: 42.txt, 1015.txt")
if choice=='D':
        file=input("Enter the filename:\n")
        if file=='42.txt':
            print("The meaning of life is blah blah blah ...")
        if file=='1015.txt':
            print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")
        elif file!='42.txt' and file!='1015.txt':
            print("File not found")


while choice!='X':
    print("Welcome to UCT BBS\nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")
    
    choice=input("Enter your selection: \n") 
    choice=choice.upper()
   
    if choice=='E' :
        message=input("Enter the message: \n")
    if choice=='V':
        if message=='':
            print("The message is: no message yet")
        else:
            print("The message is:", message)
    if choice=='L':
        print("List of files: 42.txt, 1015.txt")
    if choice=='D':
        file=input("Enter the filename:\n")
        if file=='42.txt':
            print("The meaning of life is blah blah blah ...")
        if file=='1015.txt':
            print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")
        elif file!='42.txt' and file!='1015.txt':
            print("File not found")
    else:
        if choice=='X':
            print("Goodbye!")
            break
    
    


    
        
            
        
    
