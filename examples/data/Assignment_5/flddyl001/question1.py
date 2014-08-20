'''MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:'''

print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
v_select = input("Enter your selection:\n") 
start_again = False
v_message = ""
while v_select != "X" or v_select != "x":
    
    if v_select == "E" or v_select == "e":
        v_message = input("Enter the message:\n")
        start_again = True
    elif v_select == "V" or v_select == "v":
        if v_message == "":
            print("The message is: no message yet")
        else:
            print("The message is:",v_message)
        start_again = True
    elif v_select == "L" or v_select == "l":
        print("List of files: 42.txt, 1015.txt")
        start_again = True
    elif v_select == "D" or v_select == "d":
        v_file = input("Enter the filename:\n")
        if v_file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif v_file == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
        start_again = True
    elif v_select == "X" or v_select == "x":
        break
    if start_again == True:
        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        v_select = input("Enter your selection:\n")
        start_again = False
print("Goodbye!")
        
    