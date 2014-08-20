choice=''
message='no message yet'
f1015="Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
f42="The meaning of life is blah blah blah ..."
while choice !='x':
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    choice=input("Enter your selection:\n").lower()
    
    if choice == 'x':
        print("Goodbye!")

    elif choice == 'e':
        message = input("Enter the message:\n")
    elif choice =='v':
        print("The message is:",message)
    elif choice == 'l':
        print("List of files: 42.txt, 1015.txt")
    elif choice=='d':
        c=input("Enter the filename:\n")
        if c=='1015.txt':
            print(f1015)
        elif c=='42.txt':
            print(f42)
        else: print("File not found")
else: pass
        
        