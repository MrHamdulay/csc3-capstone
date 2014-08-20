#question1.py
#Cecil Hlungwana
#HLNCEC001
#16 April 2014

menu = 0 #A variable has been set to be used later
E = 'no message yet' 
while menu !="X": #If the input is not X, it should do the following
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\n",end="")
    menu = input("Enter your selection:\n")
    if menu.upper() == "E":
        E = input("Enter the message:\n")
    elif menu.upper() == "V":
        print("The message is:",E)
    elif menu.upper() == "X":
        print("Goodbye!")
        break
    elif menu.upper() == "L":
        print("List of files: 42.txt, 1015.txt")
    elif menu.upper() == "D":
        D = input("Enter the filename:\n")
        if D == "42.txt":
            print('The meaning of life is blah blah blah ...')
        elif D == "1015.txt":
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
        else:
            print("File not found")