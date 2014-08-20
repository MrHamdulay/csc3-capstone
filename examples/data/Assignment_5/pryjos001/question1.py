"""Bulletin Board System
Joe Preyer
16 April 2014"""

# Assign stored variables

msg = 0
no_file = "File not found"
greet_menu = "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it"
ans = 0

# Receive command and give appropriate response when the user does not want to exit
while ans!= "X":
    print (greet_menu)
    ans = input("Enter your selection:\n").upper()

    if ans== "E":
        msg = input("Enter the message:\n")
        
    elif ans == "V":
        if msg==0:
            print ("The message is: no message yet")
        else:
            print ("The message is:", msg)
        
    elif ans == "L":
        print ("List of files: 42.txt, 1015.txt")
        
    elif ans == "D":
        file = input("Enter the filename:\n")
        if file == "42.txt":
            print ("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print (no_file)
    
print ("Goodbye!")
