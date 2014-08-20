"""Program to simulate a simple BBS
Tinotenda Chemvura CHMTIN004
12 April 2014"""

#__________________________Program Starts Here________________________________

ans = ""
msg = ""

while ans != "X":

    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")

    ans = input("Enter your selection:\n")
    
    ans = ans.upper()
    
    if ans == "E":
        msg = input("Enter the message:\n")

    elif ans == "V":

        if msg:
            print("The message is:",msg)
        else:
            print("The message is: no message yet")

    elif ans == "L":
        print("List of files: 42.txt, 1015.txt")

    elif ans == "D":
        fname = input("Enter the filename:\n")
        if fname == "1015.txt":
            print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        if fname == "42.txt":
            print("The meaning of life is blah blah blah ...")
        if fname != "42.txt" and fname!= "1015.txt":
            print("File not found")

    elif ans == "X":
        break

print("Goodbye!")
