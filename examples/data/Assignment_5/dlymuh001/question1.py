option = ""
msg = ""
files = ["42.txt","1015.txt"]
contents = ["The meaning of life is blah blah blah ...",
            "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"]
while option != "X" and option != "x":
    print ("Welcome to UCT BBS")
    print ("MENU")
    print ("(E)nter a message")
    print ("(V)iew message")
    print ("(L)ist files")
    print ("(D)isplay file")
    print ("e(X)it")
    option = input("Enter your selection:\n")
    if option == "E" or option == "e":
        msg = input("Enter the message:\n")
    elif option == "V" or option == "v":
        if msg == "":
            print("The message is: no message yet")
        else:
            print ("The message is:", msg)
    elif option == "L" or option == "l":
        print ("List of files:", ", ".join(files))
    elif option == "D" or option == "d":
        filename = input("Enter the filename:\n")
        if (filename in files) == True:
            i = files.index(filename)
            print (contents[i])
        else:
            print ("File not found")
    elif option == "X" or option == "x":
        print ("Goodbye!")