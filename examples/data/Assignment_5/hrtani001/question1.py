#simple text based program
#Aniq Hartle
#16-04-2014

#initialise variables
message = -1
selection = ""

#excecute and print repeated menu
while selection.lower() != "x":
    print("Welcome to UCT BBS\n\
MENU\n\
(E)nter a message\n\
(V)iew message\n\
(L)ist files\n\
(D)isplay file\n\
e(X)it")

    #get user input
    selection = input("Enter your selection:\n")
    
    #compare user input and excecute instructions accordingly
    if selection.lower() == "e":
        message = input("Enter the message:\n")
    
    elif selection.lower() == "v":
        if message!=-1:
            print("The message is:",message)
        else:
            print("The message is: no message yet")
            
    elif selection.lower() == "l":
        print("List of files: 42.txt, 1015.txt")
        
    elif selection.lower() == "d":
        fileNm = input("Enter the filename:\n")
        if fileNm == "42.txt":
            infile = open("42.txt","r")
            print(infile.read())  
        elif fileNm == "1015.txt":
            infile = open("1015.txt","r")
            print(infile.read())            
        else:
            print("File not found")

#when loop is exited by user print and end            
print("Goodbye!")