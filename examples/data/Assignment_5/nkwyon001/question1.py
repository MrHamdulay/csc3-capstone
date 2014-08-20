"""a simple BBS 
Yondela Nkwali
14 April 2014"""

#list of files
file1="42.txt"
file2="1015_txt"
#write menu
def displayMenu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

displayMenu()
selection=input("Enter your selection:\n")
if selection!="x":
    #if/else statements for options
    if selection == "E":
        ask4message=input("Enter the message:\n")
        displayMenu()
        selection=input("Enter your selection:\n")
        if selection == "V":
            print("The message is:",ask4message)
        displayMenu()
        selection=input("Enter your selection:\n")
    if selection == "V":
        print("The message is: no message yet")
        displayMenu()
        selection=input("Enter your selection:\n")     
    if selection == "L" or"l":
        print("List of files:",file1,file2)
    if selection == "D" or "d":
        fname=input("Enter the filename:\n")
        if fname==file1:
            print("The meaning of life is blah blah blah ...")
        if fname==file2:
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            displayMenu
            selection=input("Enter your selection:\n") 
        if fname!= file1 or file2:
            print("File not found")
else:
    print("Goodbye!")
            
                   