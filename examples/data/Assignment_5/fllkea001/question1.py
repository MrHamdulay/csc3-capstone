#PRogram for a simple BBS
#Keanon Fell
#15 April 2014

#Creating empty strings outside the loop so it can be ovewritten each time the user inputs something different
answer = ""
message =""

while answer != 'X':#Once the user enters X then the program will execute 
                    #whatever code is in the body of the else and then break out of the program
    
    #Printing out the menu 
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    answer = input("Enter your selection:\n")
    answer = answer.upper()#Form of data validation
    
    #Checking for all instances of the users inputs
    if answer == 'E':
        message = input("Enter the message:\n")
    elif answer == 'V':
        print('The message is:',message)
    elif answer == 'L':
        if answer != "":
            print('The message is: No message yet')
        else:
            print('List of files: 42.txt, 1015.txt')
        
    elif answer == 'D':
        file = input("Enter the filename:\n")
        if file == '42.txt':
            print('The meaning of life is blah blah blah ...')
        elif file == '1015.txt':
            print('Computer Science class notes ... simplified')
            print('Do all work')
            print('Pass course')
            print('Be happy')
        else:
            print("File not found")
    elif answer == 'X':
        print('Goodbye!')