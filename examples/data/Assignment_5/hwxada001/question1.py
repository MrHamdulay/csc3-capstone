def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")  
m = ""
f = ["42.txt", "1015.txt"]
menu()

while True:
    s = input("Enter your selection:" '\n')
    s = s.lower()
    
    if s == "e":
        m = input("Enter the message:" '\n')
        menu()
         
    elif s == "v":
        if m == "":
            print("The message is: no message yet")
        else: 
            print("The message is:", m)
        menu()
        
    elif s == "l":
        print("List of files: ", f[0], ", ", f[1],sep="")
        menu()
        
    elif s == "d":
        f = input("Enter the filename:" '\n')
        if f == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif f == "1015.txt":
            print("Computer Science class notes ... simplified" '\n' "Do all work" '\n' "Pass course" '\n' "Be happy")
        else:
            print("File not found")        
        menu()
        
    elif s == "x":
        print("Goodbye!")
        break

    
 