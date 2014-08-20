#Question 1
#Creating a BBS System in VB
#By: Dean de Haast
#14 April 2014

choice = " "
message=""


# Creating the sentinel value for ending it. 
while choice not in "xX":
    #Printing the menu.
    print("Welcome to UCT BBS")
    print("MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    choice = input("Enter your selection:\n")
    
    #Choice Selection
    if choice in"eE":
        message=input("Enter the message:\n")
        
    elif choice in"vV":
        if message =="":
            print("The message is: no message yet")
        else:
            print("The message is:",message)      
    elif choice in "lL":
        print("List of files: 42.txt, 1015.txt")
        
    elif choice in"dD":
        file_name =input("Enter the filename:\n")
        if file_name =="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file_name=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
        
        
        
        
print("Goodbye!")