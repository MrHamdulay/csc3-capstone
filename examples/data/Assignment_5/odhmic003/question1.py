print("Welcome to UCT BBS"'\n'"MENU"'\n'"(E)nter a message"'\n'"(V)iew message"'\n'"(L)ist files"'\n'"(D)isplay file"'\n'"e(X)it")
s = input("Enter your selection:"'\n') 
text="" 
while s=="e":
    text= input("Enter the message:"'\n')
    print("Welcome to UCT BBS"'\n'"MENU"'\n'"(E)nter a message"'\n'"(V)iew message"'\n'"(L)ist files"'\n'"(D)isplay file"'\n'"e(X)it")
    s = input("Enter your selection:"'\n') 

while s=="v":
    
    if len(text)>0:
        print("The message is:",text)
    else:
        print("The message is: no message yet")
    print("Welcome to UCT BBS"'\n'"MENU"'\n'"(E)nter a message"'\n'"(V)iew message"'\n'"(L)ist files"'\n'"(D)isplay file"'\n'"e(X)it")
    s = input("Enter your selection:"'\n')   
    while s=="e":
        text= input("Enter the message:"'\n')
        print("Welcome to UCT BBS"'\n'"MENU"'\n'"(E)nter a message"'\n'"(V)iew message"'\n'"(L)ist files"'\n'"(D)isplay file"'\n'"e(X)it")
        s = input("Enter your selection:"'\n')     
while s=="l":
    print("List of files: 42.txt, 1015.txt")
    print("Welcome to UCT BBS"'\n'"MENU"'\n'"(E)nter a message"'\n'"(V)iew message"'\n'"(L)ist files"'\n'"(D)isplay file"'\n'"e(X)it")
    s = input("Enter your selection:"'\n')     
while s=="d":
    file = input("Enter the filename:"'\n')
    if file=="42.txt":
        print("The meaning of life is blah blah blah ...")
    elif file=="1015.txt":
        print("Computer Science class notes ... simplified"'\n'"Do all work"'\n'"Pass course"'\n'"Be happy")
    else:
        print("File not found")
    print("Welcome to UCT BBS"'\n'"MENU"'\n'"(E)nter a message"'\n'"(V)iew message"'\n'"(L)ist files"'\n'"(D)isplay file"'\n'"e(X)it")
    s = input("Enter your selection:"'\n')     
while s=="x":
    print("Goodbye!")
    break
    