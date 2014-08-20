"""Simple BBS program
Kristin Kinmont
13 April 2014"""

# function to print out menu options
def menu():
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
message = "no message yet"
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    menu()
    s = input("Enter your selection:\n")
    s = s.upper() #convert input to UPPER CASE
    if s == "E":
        message = input("Enter the message:\n")
    if s == "V":
        print("The message is:",message)
    if s == "L":
        print("List of files: 42.txt, 1015.txt")
    if s == "D":
        y = input("Enter the filename:\n")
        if y == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif y == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    if s == "X":
        print("Goodbye!")
        break
            
    