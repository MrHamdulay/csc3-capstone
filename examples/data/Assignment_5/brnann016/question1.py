#Question 1-UCT BBS
#Annika Brundyn
#16/04/2014

menu = ("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
selection=0
message=""
while selection!="X":
    print(menu)
    selection = input( "Enter your selection:\n")
    selection = selection.upper()    
    if selection=="E":
        message=input("Enter the message:\n")
        
    if selection  == "V" and message == "":
        print( "The message is: no message yet")
        
    if selection == "V" and message != "":
        print( "The message is:", message) 
            
    elif selection=="L":
        print("List of files: 42.txt, 1015.txt")
        
    elif selection=="D":
        file=input("Enter the filename:\n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
                
if selection=="X":
    print("Goodbye!")

    