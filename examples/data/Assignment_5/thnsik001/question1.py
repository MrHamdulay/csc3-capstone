"""Question1 Assignment5
Skhulile Thenjwayo
16 April 2014"""

#  outputing menu in indefinate loop
message ="no message yet"
character = "" 
search= ""
while character != "X":
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    character = input("Enter your selection:\n").upper()
    if character == "E":
        message = input("Enter the message:\n")
    elif character == "V":
        print("The message is:",message)
    elif character == "L":
        print("List of files: 42.txt, 1015.txt")
    elif character == "D":
        search = input("Enter the filename:\n")
        if search == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif search == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
print("Goodbye!")