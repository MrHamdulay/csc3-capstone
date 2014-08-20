
def menu():
    choice="none"    
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    selection()    

def selection():
    global msg
    choice=input("Enter your selection:\n").upper()
    if choice=="E":
        msg=input("Enter the message:\n")
        menu()
    elif choice=="V":
        print("The message is:",msg)
        menu()
    elif choice=="L":
        print("List of files: 42.txt, 1015.txt")
        menu()
    elif choice=="D":
        choice=input("Enter the filename:\n")
        if choice=="42.txt":
            print("The meaning of life is blah blah blah ...")
            menu()
        elif choice=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy ") 
            menu()
        else:
            print("File not found")
            menu()
    elif choice=="X":
        print("Goodbye!")
msg="no message yet"
menu()
    
    