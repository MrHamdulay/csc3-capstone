'''Q1 of Assignment 5: Bulletin Board System to exchange messages and files
Patrick Boroughs
16 April 2014'''

message='no message yet'
choice=''

while True:
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:")
    
    choice=input("")
    
    if choice.upper()=='E':
        message=input("Enter the message:\n")
        
    elif choice.upper()=='V':
        print("The message is:",message)
    
    elif choice.upper()=='L':
        print("List of files: 42.txt, 1015.txt")
    
    elif choice.upper()=='D':
        file=input("Enter the filename:\n")
        if file=='42.txt':
            print("The meaning of life is blah blah blah ...")
        elif file=='1015.txt':
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    elif choice.upper()=='X':
        print("Goodbye!")
        break
    

