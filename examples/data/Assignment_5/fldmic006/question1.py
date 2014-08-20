#menu system
#michael field
#15 april 2014

#declare variables
choice = ''
file1 = "42.txt"
file2 = "1015.txt"
message = ''

#loop menu options until exit is chosen
while (choice != 'X'):
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    
    #get menu option chosen and convert to uppercase
    choice = input("Enter your selection:\n")
    choice = choice.upper()
    
    if (choice == 'E'):
        message = input("Enter the message:\n")
    
    elif(choice == 'V'):
        
        if (message == ''):
            print("The message is: no message yet")
       
        else:
            print("The message is:", message)
    
    elif(choice == 'L'):
        print("List of files: ", file1, ", ", file2, sep = '')
    
    elif(choice == 'D'):
        filename = input("Enter the filename:\n")
        
        if (filename == file1):
            print("The meaning of life is blah blah blah ...")
        
        elif (filename == file2):
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        
        else:
            print("File not found")
    #end while loop
    
print("Goodbye!")