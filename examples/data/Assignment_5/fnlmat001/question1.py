"""program that simulates a simple BBS with one stored message and 2 fixed files
Matthew Finlayson - FNLMAT001
15/04/2014"""

message ="no message yet"
file1 = "The meaning of life is blah blah blah ..."
file2 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"

while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    s = input("Enter your selection:\n")
    
    if (s[0].upper() == "E"):
        msg = input("Enter the message:\n")
        message = msg
    
    elif(s[0].upper() == "V"):
        print("The message is:", message)
       
    elif(s[0].upper() == "L"):
        print("List of files: 42.txt, 1015.txt")
        
    elif(s[0].upper() == "D"): #prompts user to enter a filename and checks to see if the file exists, then displays it
        fileName = input("Enter the filename:\n")
        if (fileName == "42.txt"):
            print(file1)
        elif (fileName == "1015.txt"):
            print(file2)
        else: print("File not found")
    
    elif(s[0].upper() == "X"):
        print("Goodbye!")
        break
    