'''BBs program
Mokoena Mafologele
16/04/2014'''



choice=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
choice=choice.upper()
message=""
while(choice!="X"):
    files=["42.txt","1015.txt"]
    if choice=="E":
        message=input("Enter the message:\n")
    elif choice=="V":
        print("The message is: ",end="")
        if len(message)>0:
            print(message)
        else:
            print("no message yet")
    elif choice=="L":
        print("List of files: ",files[0],", ", files[1],sep="")
    else:
        fname=input("Enter the filename:\n")
        if fname==files[1]:
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        elif fname==files[0]:
            print("The meaning of life is blah blah blah ...")
        else:
            print("File not found")
    choice=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    choice=choice.upper()
print("Goodbye!")
