#Rorisang Moseli
#April 2014
#Basic BBS Program

#set the choice to begin the loop
choice="o"
#default message
message= "no message yet"

while choice!= "x":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice = input("Enter your selection:\n")
    choice = choice.lower()
    if choice == "e":
        message = input("Enter the message:\n")
    elif choice == "v":
        print("The message is:", message)
    elif choice == "l":
        print("List of files: 42.txt, 1015.txt")
    elif choice == "d":
        file=input("Enter the filename:\n")
        if file=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
print("Goodbye!")

    