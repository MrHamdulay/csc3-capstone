#Assignment 5, Question 1
#UCT BBS Program
#Tejasvin Bagirathi BGRTEJ001
#2014-04-17

txt1 = "The meaning of life is blah blah blah ..."
txt2 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
message = "no message yet"
selection = "b"
while (selection != "x"):
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    #User chooses an option
    selection = input("Enter your selection:\n")
    selection = selection.upper()
    #User enters a messsage
    if selection == 'E':
        message = input("Enter the message:\n")
    #Displays users message
    elif selection == 'V':
        print("The message is: " + message)
    #Lists available files
    elif selection == 'L':
        print("List of files: 42.txt, 1015.txt")
    #Allows user to choose file to be displayed
    elif selection == 'D':
        filename = input("Enter the filename:\n")
        if filename == '1015.txt':
            print(txt2)
        elif filename == '42.txt':
            print(txt1)
        else: print("File not found")
    #Exit loop
    else: 
        if selection == 'X': break
        
print("Goodbye!")

