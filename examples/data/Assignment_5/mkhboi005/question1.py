""" Tumi Mkhawana
15 April 2014"""


print("Welcome to UCT BBS\nMENU")
print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
selection = input("Enter your selection:\n")
message = "no message yet" 

#create a while loop to continue asking the user to enter selection
#make selection upper case
while selection.upper() != "X":
    if selection.upper() == "L":
        print("List of files: 42.txt, 1015.txt")
    if selection.upper() =="D":
        filename= input("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
            
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            
        else: 
            print("File not found")
#selection of v
    if selection.upper() == "V":
        print("The message is:", message) 
    #selection of E
    if selection.upper() == "E":
        message = input("Enter the message:\n")
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    selection = input("Enter your selection:\n")
   
        
#print goodbye to end program
else:
    print("Goodbye!")
    