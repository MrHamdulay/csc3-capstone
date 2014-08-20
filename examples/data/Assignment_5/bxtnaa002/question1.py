# question1.py
# program to stimulate a simple BBS
# author: bxtnaa002


print("Welcome to UCT BBS"+"\n"+"MENU"+"\n"+"(E)nter a message"+"\n"+"(V)iew message"+"\n"+"(L)ist files"+"\n"+"(D)isplay file"+"\n"+"e(X)it") #print the menu and allow user to input selection
answer = input("Enter your selection:\n")
message="" #set the default message as an empty string in case user chooses "v" and has not typed in a message to be stored 

#indefinite loops are incorporated with each selection to allow program to keep printing out menu after the contents of each selection has been outputed.
while answer == "e": 
    message = input("Enter the message:\n")
    print("Welcome to UCT BBS"+"\n"+"MENU"+"\n"+"(E)nter a message"+"\n"+"(V)iew message"+"\n"+"(L)ist files"+"\n"+"(D)isplay file"+"\n"+"e(X)it")
    answer = input("Enter your selection:\n") 
    
while answer == "v": 
    if len(message) > 0: #prints out inputed message
        print("The message is: "+message)
    else:  #else if user has not inputed message
        print("The message is: no message yet") 
    print("Welcome to UCT BBS"+"\n"+"MENU"+"\n"+"(E)nter a message"+"\n"+"(V)iew message"+"\n"+"(L)ist files"+"\n"+"(D)isplay file"+"\n"+"e(X)it")
    answer = input("Enter your selection:\n")
    while answer == "e":
        message = input("Enter the message:\n")
        print("Welcome to UCT BBS"+"\n"+"MENU"+"\n"+"(E)nter a message"+"\n"+"(V)iew message"+"\n"+"(L)ist files"+"\n"+"(D)isplay file"+"\n"+"e(X)it")
        answer = input("Enter your selection:\n")     
   
while answer == "l":
    print("List of files: 42.txt, 1015.txt")
    print("Welcome to UCT BBS"+"\n"+"MENU"+"\n"+"(E)nter a message"+"\n"+"(V)iew message"+"\n"+"(L)ist files"+"\n"+"(D)isplay file"+"\n"+"e(X)it")
    answer = input("Enter your selection:\n")
    
while answer == "d":
    filename = input("Enter the filename:\n")
    if filename == "42.txt": # 2 fixed filenames
        print("The meaning of life is blah blah blah ...")
    elif filename == "1015.txt":
        print("Computer Science class notes ... simplified", "Do all work", "Pass course", "Be happy", sep="\n")
    elif filename != "42.txt" or filename !="1015.txt":
        print("File not found") #when user inputs filename that is neither of the 2 fixed
    print("Welcome to UCT BBS"+"\n"+"MENU"+"\n"+"(E)nter a message"+"\n"+"(V)iew message"+"\n"+"(L)ist files"+"\n"+"(D)isplay file"+"\n"+"e(X)it")
    answer = input("Enter your selection:\n")    

while answer == "x": 
    print("Goodbye!")
    break #when user makes a selection of "x" program stops running