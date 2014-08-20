#Assignment 5
#Question 1
#Barry Su
#15 April 2014

#define the main function
def main():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
main()  #run main function

selection = input("Enter your selection: \n")
selection = selection.upper()
msg = "no message yet"
#create a while loop 
while selection != "X":
    if selection == "E":
        msg = input("Enter the message: \n")
    elif selection == "V":
        print("The message is:", msg)
    elif selection == "L":
        print("List of files: 42.txt, 1015.txt")
    elif selection == "D":
        fname = input("Enter the filename:\n")
        if fname == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif fname == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    main()
    selection = input("Enter your selection: \n")
    selection = selection.upper()
print("Goodbye!")