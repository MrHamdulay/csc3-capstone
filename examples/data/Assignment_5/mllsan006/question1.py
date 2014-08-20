'''Assignment 5 Question 1
Sankara Mallane
14 April 2014'''

userInput = ''
userMessage = "no message yet"

while userInput != ('x').upper():
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    
    userInput = (input("Enter your selection:\n")).upper()
    
    if userInput == "E":
        userMessage = input("Enter the message:\n")
        
    if userInput == 'V':
        print("The message is: " + userMessage)

    if userInput == 'L':
        print("List of files: 42.txt, 1015.txt")
        
    if userInput == 'D':
        fileName = input("Enter the filename:\n")
        
        if fileName == "42.txt":
            print("The meaning of life is blah blah blah ...")
       
        elif fileName == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    
    if userInput == 'X':
        print("Goodbye!")
