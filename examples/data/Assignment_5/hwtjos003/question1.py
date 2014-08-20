#UCT BBS 
#Joshua Hewitson
#4/16/2014

# set default variables 
message = "no message yet"
run = True

# Keep looping the program untill the user exits (entering X or x will set run to false)
while run == True:
    
    # Print out opening message and Menu with information about options:
    print("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")

    # users choice set to string value 'selection' :
    selection = input("Enter your selection:\n")

    # Entering a message
    if selection == "E" or selection == "e":
        message = input("Enter the message:\n")
    
    # Viewing a message (if no message has been entered, the default is set to 'no message yet'    
    if selection == "V" or selection == "v":
        print("The message is:", message)
    
    # Displaying .txt file text    
    if selection == "D" or selection == "d":
        filename = input("Enter the filename:\n")
        try:
            f = open(filename)
            data = f.read()
            f.close()
            print(data)
        # if the file name entered is incorrect or dosen't exist:
        except:
            print("File not found")
            
    # print out list of known files    
    if selection == "L" or selection == "l":
        print("List of files: 42.txt, 1015.txt")

    # Exits the program by setting run to false:    
    if selection == "X" or selection == "x":
            print("Goodbye!")
            run = False