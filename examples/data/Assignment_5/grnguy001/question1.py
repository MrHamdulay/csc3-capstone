#BBS
#Done by Guy Green
#For Assignment 5
#For Funzies
m=1
message="no message yet"
file="File not found"
files=["42.txt", "1015.txt"]
while m!="x":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    m=input("Enter your selection:\n")
    m=m.lower()
    if m=="e":
        message=input("Enter the message:\n")
    elif m=="v":
        print("The message is:", message)
    elif m=="l":
        print("List of files: 42.txt, 1015.txt")
    elif m=="d":
        display=input("Enter the filename:\n")
        if display=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        elif display=="42.txt":
            print("The meaning of life is blah blah blah ...")
        else:
            print(file)
print("Goodbye!")   
