"""UCT Bulletin Board Systems(BBS) simulation
peter m muriuki"""
msg=""
while True:
    print("Welcome to UCT BBS"+"\nMENU"+"\n(E)nter a message"+"\n(V)iew message"+"\n(L)ist files"+"\n(D)isplay file"+"\ne(X)it")
    selc=input("Enter your selection:\n")
    selc=selc.lower()
    if selc=="e":
        msg+=input("Enter the message:\n")
    elif selc=="v":
        if msg=="":
            print ("The message is: no message yet")
        else:
            print ("The message is:",msg)
    elif selc=="l":
        print ("List of files: 42.txt, 1015.txt")
    elif selc=="d":
        file=input("Enter the filename:\n")
        if file=="42.txt":
            print ("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print ("Computer Science class notes ... simplified"+"\nDo all work"+"\nPass course"+"\nBe happy")
        elif file !="42.txt" or file!="1015.txt":
            print ("File not found")
    elif selc=="x":
        print("Goodbye!")
        break
