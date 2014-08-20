#Charlie Shang
#Question 1 Assignment 5
#15 April 2014

option = '' 
sOut ="no message yet"
while option != "X": #while the user chooses to not exit the BBS
    
    option = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n").upper() #ensures the user's option is an upper case  character so that later comparisons are easier
    
    if option == "E":
        sOut = input("Enter the message:\n")
    
    if option == "V":
        print("The message is: "+ sOut)
    
    if option == "L":
        print("List of files: 42.txt, 1015.txt") #given text files
    
    if option == "D":
        x = input("Enter the filename:\n")
        if x == "42.txt":
            print("The meaning of life is blah blah blah ...") 
        elif x == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    

print("Goodbye!") #prints when the user exits