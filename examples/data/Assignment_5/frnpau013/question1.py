message = "no message yet"

selection = ""

file1_name = "42.txt"

file2_name = "1015.txt"

file1 = "The meaning of life is blah blah blah ..."

file2 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"


while selection.upper() != "X":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

    selection = input("Enter your selection:\n")

    if selection.upper() == "E":
        message = input("Enter the message:\n")
        continue
    
    elif selection.upper() == "V":
        print("The message is:", message)
        continue
    
    elif selection.upper() == "L":
        print("List of files: ", file1_name, ", ", file2_name, sep = "")
        continue
    
    elif selection.upper() == "D":
        file_selection = input("Enter the filename:\n")
        if file_selection == file1_name or file_selection == file2_name:
            if file1_name == file_selection:
                print(file1)
            if file2_name == file_selection:
                print(file2)
        else:
            print("File not found")
        continue
    elif selection.upper() == "X":
        print("Goodbye!")