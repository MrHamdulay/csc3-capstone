#Author: NLXALE001
#Date: 15 April 2014
#Assignment 5

select = "A"
#loop to continue while select id not X
message = "no message yet"
while select != "X" and select != "x":
    print ("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    select = input("Enter your selection:\n")
    #determine which option was selected
    if select == "E" or select == "e":
        message = input("Enter the message:\n")
    elif select == "V" or select == "v":
        print ("The message is:", message)
    elif select == "L" or select == "l":
        print ("List of files: 42.txt, 1015.txt")
    elif select == "D" or select == "d":
        display = input("Enter the filename:\n")
        if display == "1015.txt":
            print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        elif display == "42.txt":
            print ("The meaning of life is blah blah blah ...")
        else:
            print ("File not found")
    
print ("Goodbye!")