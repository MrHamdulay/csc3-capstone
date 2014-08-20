''' BBS simulator
Tim Mostert
16 04 2014'''

userinput = ""

message = "no message yet"

listoffiles = "42.txt, 1015.txt"

while userinput != ('X') and userinput != 'x':
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    userinput = input("Enter your selection:\n")
    if userinput == "E" or userinput == 'e':
        message = input("Enter the message:\n")
    elif userinput == "V" or userinput == 'v':
        print("The message is:",message)
    elif userinput == "L" or userinput == 'l':
        print("List of files:", listoffiles)
    elif userinput == "D" or userinput == 'd':
        filename = input("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    
print("Goodbye!")