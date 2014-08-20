# program to simulate a simple BBS
# by: khadeejah omar
# 13 april 2014

e = "(E)nter a message"
v = "(V)iew message"
l = "(L)ist files"
d = "(D)isplay file"
x = "e(X)it"
ListFile = ["42.txt", "1015.txt"]

select = 1
while select != x[2] : # loop until user exits
    
    print("Welcome to UCT BBS \n" + "MENU \n" + e + "\n" + v + "\n" + l + "\n" + d + "\n" + x) # Display welcome messsage and options to select
    select = input("Enter your selection: \n")
    select = select.upper() 

    if select == e[1] :
        message = input("Enter the message: \n")
    elif select == v[1] :
        try :
            print("The message is: " + message)
        except NameError : # if the user didnt input a message
            print("The message is: no message yet")
    elif select == l[1] :
        ListString = ", ".join(ListFile)
        print("List of files: " + ListString)
    elif select == d[1] :
        FileName = input("Enter the filename: \n")
        if FileName == "42.txt" :
            print("The meaning of life is blah blah blah ...")
        elif FileName == "1015.txt" :
            print("Computer Science class notes ... simplified \n" + "Do all work \n" + "Pass course \n" + "Be happy")
        else : # if user inputs the name of a file that wasnt defined
                print("File not found")
    elif select == x[2] :
            print("Goodbye!")