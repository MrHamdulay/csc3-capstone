#question1
#Micaela Menegaldo

def menu(message):
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    choice=input("Enter your selection:\n")
    choice=choice.capitalize()
    action(choice,message)

def action(choice,message):
    if choice=="X":
        print("Goodbye!")
    else:
        if choice in "EVLD":
            if choice=="E":
                message=input("Enter the message:\n")

            elif choice=="V":
                if message=="":
                    print("The message is: no message yet")

                else:
                    print("The message is: "+message)

            elif choice=="L":
                print("List of files: 42.txt, 1015.txt")

            elif choice=="D":
                filename=input("Enter the filename:\n")
                if filename=="42.txt":
                    print("The meaning of life is blah blah blah ...")

                elif filename=="1015.txt":
                    print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                else:
                    print("File not found")
            menu(message)
                    
if __name__=='__main__':
    message=""
    menu("")
    
