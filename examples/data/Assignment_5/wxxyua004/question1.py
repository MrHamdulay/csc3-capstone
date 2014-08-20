#Some sort of programme with 2 definite files 42.txt, and 1015.txt
#The user basically has 4 functions: Enter a message, View message, List files, and Display files
#Finally, the user can exit ii by a simple input of X.
#Things to take note of. 1 = List of files
#input of d = a response from the programme asking for either the 42.txt or 1015.txt
#42.txt = The meaning of life is blah blah blah ...
#1015.txt =
#Computer Science class notes ... simplified
#Do all work
#Pass course
#Be happy
selection = 0
message = 0
while selection !="X":
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        selection=input("Enter your selection: \n")
        selection=selection.upper()
        if selection == "E":
                message=input("Enter the message: \n")
        elif selection == "V":
                if message==0:
                        print("The message is: no message yet")
                else:
                        print("The message is:",message)
        elif selection == "L":
                print("List of files: 42.txt, 1015.txt")
                      
        elif selection == "D":
                filename=input("Enter the filename: \n")
                
                if filename == "42.txt":
                        print("The meaning of life is blah blah blah ...")
                elif filename == "1015.txt":
                        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                else:
                        print("File not found")
print("Goodbye!")
                