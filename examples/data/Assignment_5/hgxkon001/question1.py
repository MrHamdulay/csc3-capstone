#Konrad Hugo wrote this
#HGXKON001
#17/04/2014
#Question 1 Assignment 5


ans=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n") #Initial input line to start the process
 
while ans!='x' and ans!='X': #while loop because it is indefinite when the menu must stop appearing
    mes='no message yet'
    if ans=='E' or ans=='e': 
        mes=input("Enter the message:\n")
        ans=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n") #this reprints the menu
    if ans=='V' or ans=='v':
        print("The message is:",mes)
        ans=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n") #Reprints the menu
    if ans=='L' or ans=='l':
        print("List of files: 42.txt, 1015.txt") #If the input is l or L then print two file names
        ans=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")#Reprints menu(You want it to repeat popping up until the user exits manually by input x/X)
    if ans == 'D' or ans == 'd':
        file=input("Enter the filename:\n")
        if file=='1015.txt':
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        elif file=='42.txt':
            print("The meaning of life is blah blah blah ...")
        else:
            print("File not found")
        ans=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
if ans=='x' or ans=='X': #New line(Separate from loop) because it is the only input thatwill end the loop
    print("Goodbye!")
        
   
    