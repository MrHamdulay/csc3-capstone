
#Tadie
#number one..... im so worried about how to even start



message = "no message yet"
while True:
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    text = input("Enter your selection:\n")
    if text.lower() == "e":
        message = input("Enter the message:\n")
    elif text.lower() == "v":
        print("The message is:", message)
    elif text.lower() == "l":
        print("List of files: 42.txt, 1015.txt")
    elif text.lower() == "d":
        text = input("Enter the filename:\n")
        if text == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif text == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else: print("File not found")
    elif text.lower() == "x":
        print("Goodbye!")
        break
        
        
