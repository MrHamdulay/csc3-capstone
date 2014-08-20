'''program to simulate BBS
ethan jackson
16 april 2014'''

BBS = "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it"
message="no message yet"
#make select a string so it can enter the loop
select = "word"
#specific conditions if e(X)it is not chosen
while select not in ["x", "X"]:
    print(BBS) #the menu is printed 
    select = input("Enter your selection:\n")
    if select == "E" or select == "e":
        message = input("Enter the message:\n")
    elif select == "V" or select == "v":
        print("The message is:",message)
    elif select == "l" or select == "L":
        print("List of files: 42.txt, 1015.txt")
    elif select == "d" or select == "D":
        filename = input("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified\n Do all work\n Pass course\n Be happy")
        else:
            print("File not found")
#if e(X)it is chosen, then:            
print("Goodbye!")           
            
         
    