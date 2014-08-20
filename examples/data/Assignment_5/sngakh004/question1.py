#Akhil Singh
#13 April 2014
#Assignment 5
#Question 1

print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
sel = input("Enter your selection:\n")
sel=sel.upper()
msg= "The message is: no message yet"
while sel!= "X":
    if sel=="":
        print(msg)
    if sel == "E":
        msg=input("Enter the message:\n")
        msg="The message is: "+msg
    if sel=="V":
        print(msg)
    if sel=="L":
        print("List of files: 42.txt, 1015.txt")
    if sel=="D":
        filename=input("Enter the filename:\n")
        if filename=="42.txt":
            print("The meaning of life is blah blah blah ...")
        if filename=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        if filename!= "42.txt" and filename!="1015.txt":
            print("File not found")
    
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    sel = input("Enter your selection:\n")
    sel=sel.upper()
print("Goodbye!")    