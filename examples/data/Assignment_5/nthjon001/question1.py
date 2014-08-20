# BBS
# Jonathan Nathan
# 12 April 2014

selection = ''
enter_message=''
while selection != 'X':
    selection=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    selection=selection.upper()
    if selection == 'E':
        enter_message = input("Enter the message:\n")
    elif selection == 'V':
        if enter_message != '':
            print("The message is: ", enter_message,sep='')
        else: print("The message is: no message yet")
    elif selection == 'L':
        print("List of files: 42.txt, 1015.txt")
    elif selection == 'D':
        filename = input("Enter the filename:\n")
        if filename == '42.txt':
            print("The meaning of life is blah blah blah ...")
        elif filename == '1015.txt':
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else: print("File not found")
print("Goodbye!")