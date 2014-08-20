''' Assignment 5 Question 1
Matshepo Malatji
15 April 2014'''

#Display Menu and get input
print("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")
selection = input("Enter your selection:\n")
#defaults
message = "no message yet"
files = ["42.txt","1015.txt"]

#process selections
while selection.upper() != "X":

    if selection.upper() == "E":
        message = input('Enter the message:\n')
    if selection.upper() == "V":
        print("The message is: " + message)
    if selection.upper() == "L":
        print("List of files: ", end='')
        
        for i in range(len(files)-1):
            print(files[i], end=', ')
            
        print(files[len(files)-1])
        
    if selection.upper() == "D":
        filename = input("Enter the filename:\n")
        if filename not in files:
            print("File not found")
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")
        elif filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
            
    print("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")
    selection = input("Enter your selection:\n")

else:
    print("Goodbye!")