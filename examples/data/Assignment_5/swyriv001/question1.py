"""program to operate particular tasks
   Rivoningo Seweya
   14 April 2014"""
#while loop for selection choices
selection=True
msg =str("no message yet")
while selection != "X" and selection!="x":
    print("Welcome to UCT BBS""\n""MENU")
    #menu options
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    selection=(input("Enter your selection:\n"))
    if selection== "E" or selection=="e":
        msg=input("Enter the message:\n") 
    elif selection=="V" or selection=="v":
        print("The message is:",msg)
    elif selection=="L" or selection=="l":
        print("List of files: 42.txt, 1015.txt")
    elif selection=="d" or selection=="D":
        file=input("Enter the filename:\n")        
        if file=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    elif selection=="X" or selection=="x":
        print("Goodbye!")
        #break