given = ""
message = "no message yet"
files = ["42.txt","1015.txt"]
a = "The meaning of life is blah blah blah ..."
b = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
while given != 'X':
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    given = input("Enter your selection:\n").upper()
    if given == 'E':
        message = input("Enter the message:\n")
    elif given == 'V':
        print("The message is: "+message)
    elif given == 'L':
            print("List of files: "+files[0] +', ' + files[1])
    elif given == 'D':
        fn = input("Enter the filename:\n")
        if fn in files:
            if fn == files[0]:
                print(a)
            if fn == files[1]:
                print(b)            
        else:
            print("File not found")
else:
    print("Goodbye!")
