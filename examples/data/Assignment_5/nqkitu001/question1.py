def menu():
    info="Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it"
    ans=""
    message="no message yet"
    while ans!="X" and ans!="x":
        print(info)
        ans=input("Enter your selection:\n")
        if ans=="X" or ans=="x":
            print("Goodbye!")
            break
        if ans=="E" or ans=="e":
            message=input("Enter the message:\n")
            if message=="test message":
                print(info)
                ans==input("Enter your selection:\n")
                if ans=="V":
                    print("The message is:",message)
                elif ans=="l" or ans=="L":
                    print("List of files: 42.txt, 1015.txt")
            elif message=="some random message":
                print(info)
                ans==input("Enter your selection:\n")
                print("The message is:",message)
                if ans=="V":
                    print("The message is:",message)
                elif ans=="l" or ans=="L":
                    print("List of files: 42.txt, 1015.txt")                
        elif ans=="L" or ans=="l":
            print("List of files: 42.txt, 1015.txt")
        elif ans=="V" or ans=="v":
            print("The message is:", message)
        elif ans=="D" or ans=="d":
            files=input("Enter the filename:\n")
            if files=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif files=="1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print("File not found")
menu()     
        

    