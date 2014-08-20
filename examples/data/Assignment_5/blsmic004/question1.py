''' public BBS program
Michele Balestra BLSMIC004
17 April 2014'''

message = ''
while True: 
    selection = input ("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it \nEnter your selection:\n")
    # if statements depending on the users input
    if selection == 'E' or selection == 'e':
        message = input("Enter the message:\n")
    elif selection == 'V' or selection == 'v':
        if message:
            print ("The message is:", message)
        else:
            print("The message is: no message yet")
    elif selection == 'L' or selection == 'l':
        filelist = ["42.txt","1015.txt"]
        print("List of files: ", filelist[0], ', ', filelist[1], sep='')
    elif selection == 'D' or selection == 'd':        
        filename = input("Enter the filename:\n")
        # if user input matches file name or not
        if filename in filelist:
            file = open(filename,"r")
            display = file.read()
            print(display)
            file.close()
        else:
            print("File not found")
    else: 
        print("Goodbye!")
        break