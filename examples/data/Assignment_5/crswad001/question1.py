def introl():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")    
introl()
choice1 = input("Enter your selection:\n")
a = "The meaning of life is blah blah blah ..."
choice = choice1.upper()
y = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
if choice == "X":
    print("Goodbye!")
msg=""
while choice != "X":
    while choice == "E":
        msg += input("Enter the message:\n")
        introl()
        choice1 = input("Enter your selection:\n")   
        choice = choice1.upper()
        if choice == "X":
            print("Goodbye!")
        break
    while choice == "V":
        if msg == "":
            print("The message is:", "no message yet")
        else: 
            print("The message is:", msg)
        introl()
        choice1 = input("Enter your selection:\n")
        choice = choice1.upper()
        if choice == "X":
            print("Goodbye!")
        break
    while choice == "L":
        print("List of files:","42.txt, 1015.txt")
        introl()  
        choice1 = input("Enter your selection:\n")
        choice = choice1.upper()
        if choice == "X":
            print("Goodbye!")        
        break
    while choice == "D":
        file = input("Enter the filename:\n")
        if file == "42.txt":
            print(a)
            introl()
            choice1 = input("Enter your selection:\n")
            choice = choice1.upper()
            if choice == "X":
                print("Goodbye!")   
            break
            

        if file == "1015.txt":
            print(y)
            introl()          
            choice1 = input("Enter your selection:\n")
            choice = choice1.upper()
            if choice == "X":
                print("Goodbye!")
            break
        else:
            print("File not found")
            introl()
            choice1 = input("Enter your selection:\n")   
            choice = choice1.upper()
            if choice == "X":
                print("Goodbye!")  
            break
        break
        

