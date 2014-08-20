#question 1 assignment 5
#Shane Horsley
#14 April 2014

#initial print statement (could maybe have used a variable to be more efficient)
print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
choice1 = input("Enter your selection:\n")
choice = choice1.upper() #to allow for lower and upper case input
a = "The meaning of life is blah blah blah ..." #2 "FILES"
y = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
if choice == "X":
    print("Goodbye!")
msg=""
while choice != "X": #loop if initial input isnt x
    while choice == "E": #same process for each nested loop
        msg += input("Enter the message:\n")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        choice1 = input("Enter your selection:\n")   
        choice = choice1.upper()
        if choice == "X":
            print("Goodbye!")
        break
    while choice == "V":
        if msg == "": #if V is selected before E
            print("The message is:", "no message yet")
        else: 
            print("The message is:", msg)
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        choice1 = input("Enter your selection:\n")
        choice = choice1.upper()
        if choice == "X":
            print("Goodbye!")
        break
    while choice == "L":
        print("List of files:","42.txt, 1015.txt")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")   
        choice1 = input("Enter your selection:\n")
        choice = choice1.upper()
        if choice == "X":
            print("Goodbye!")        
        break
    while choice == "D":
        file = input("Enter the filename:\n")
        if file == "42.txt":
            print(a)
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
            choice1 = input("Enter your selection:\n")
            choice = choice1.upper()
            if choice == "X":
                print("Goodbye!")   
            break
            

        if file == "1015.txt":
            print(y)
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")          
            choice1 = input("Enter your selection:\n")
            choice = choice1.upper()
            if choice == "X":
                print("Goodbye!")
            break
        else:
            print("File not found")
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
            choice1 = input("Enter your selection:\n")   
            choice = choice1.upper()
            if choice == "X":
                print("Goodbye!")  
            break
        break
        

