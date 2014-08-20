message="The message is: no message yet"
while True:
#Menu and Welcome
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    choice=input("Enter your selection:\n")
    choice=choice.lower()
    #print(choice)
    
    if choice=="e":
        message=input("Enter the message:\n")
        message="The message is: "+message
        #return message

    elif choice=="v":
        print(message) 
        #continue

    elif choice=="l":
        print("List of files: 42.txt, 1015.txt")
        #continue 
    
    elif choice=="d":
        file=input("Enter the filename:\n")
        if file=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
            #continue
    elif choice=="x":
        print("Goodbye!")
        break 