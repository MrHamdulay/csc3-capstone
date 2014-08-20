"""Question 1-Assignment 5
FRNHAN004
16 April 2014"""

while True: #loop
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    x=input("Enter your selection:\n") #get input

#output depending on the user input
    if x=='E' or x=='e': 
        message=input("Enter the message:\n")
    if x=='V' or x=='v':
        try:
            print("The message is:",message)
        except:
            print("The message is: no message yet")
    if x=='L' or x=='l':
        print("List of files: 42.txt, 1015.txt")
    if x=='D' or x=='d':
        y=input("Enter the filename:\n")
        if y=='42.txt':
            print("The meaning of life is blah blah blah ...")
        elif y=='1015.txt':
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    if x=='X' or x=='x':
        print("Goodbye!") #end the loop
        break
        
