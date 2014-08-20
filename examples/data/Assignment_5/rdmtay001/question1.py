#BBS
#Tayla Radmore
#15 April 2014

#creating empty lists
messages=''



selection="a"
while selection != "X" or selection !="x":

#print out menu and get in put
#def menu():
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection=input("Enter your selection:\n")
    



    # to enter a message

    if selection=="E" or selection=="e":
        new_message=input("Enter the message:\n")
        messages= messages + new_message
    
    
    #to view message
    if selection=="V" or selection=="v":
        if messages:
            print("The message is:",new_message)
        else:
            print("The message is: no message yet")
            
    
    # to list files
    if selection=="L" or selection=="l":
        print("List of files: 42.txt, 1015.txt")
       
    #to display a file
    if selection=="D" or selection=="d":
        file=input("Enter the filename:\n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
        
    if selection=="X" or selection=="x": break
# when exited   
print("Goodbye!")
        
        
        
    



  