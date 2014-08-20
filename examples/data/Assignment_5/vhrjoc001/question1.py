#Jocelyn
#question 1
#making a bbs 
#Jocelyn
#question 1
#making a bbs 
message="no message yet"
menu=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
while menu!="X" or menu!="x":
        if menu=="E"or menu=="e":
                message=input("Enter the message:\n")
        #menu=input("Welcome to UCT BBS\n MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
        elif menu=="V"or menu=="v":
                print("the message is :",message)
        #menu=input("Welcome to UCT BBS\n MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
        elif menu=="L"or menu=="l":
                print("List of files: 42.txt, 1015.txt")
        #menu=input("Welcome to UCT BBS\n MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")    
        elif menu=="d" or menu=="D":
                choice=input("Enter the filename:\n")
                if choice =="42.txt":
                        print("The meaning of life is blah blah blah ...")
                elif choice=="1015.txt":
                        print("Computer Science class notes ... simplified","\nDo all work","\nPass course","\nBe happy")
                elif choice!="42.txt" or choice!="1015.txt":
                        print("File not found")    
        menu=menu.lower()
        if menu=="x":
                break
        else:
                menu=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
       

print("Goodbye!")    












"""menu=input("Welcome to UCT BBS\n MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
if menu=="E"or menu=="e":
        message=input("Enter the message:\n")
menu=input("Welcome to UCT BBS\n MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
elif menu=="V"or menu=="v":
        print("the message is :",message)
menu=input("Welcome to UCT BBS\n MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
elif menu=="L"or menu=="l":
        print("List of files: 42.txt,1015.txt")
menu=input("Welcome to UCT BBS\n MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")    
elif menu=="d" or menu=="D":
        choice=input("Enter the filename:\n")
        if choice =="42.txt":
        print("The meaning of life is blah blah blah...")
elif choice=="1015.txt":
        print("Computer science class notes ... simplified","\nDo all work","\nPass course","\nBe happy")
elif choice!="42.txt" or choice!="1015.txt":
        print("File not found")    
    menu=input("Welcome to UCT BBS\n MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")    
elif menu=="X" or menu=="x":
        print("Goodbye")"""   