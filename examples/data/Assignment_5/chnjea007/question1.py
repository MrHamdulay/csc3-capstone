selection = ""
files = ["42.txt", "1015.txt"]
contents = ["The meaning of life is blah blah blah ...", "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"]
message = "no message yet"
def options(choice):
    if choice.upper() == "E":
        global message
        message = input("Enter the message:\n")
    if choice.upper() == "V":
        print("The message is:", message)
    if choice.upper() == "L":
        print("List of files: ", files[0], ", ", files[1], sep = "")
    if choice.upper() == "D":
        filename = input("Enter the filename:\n")
        for i in range(len(files)):
            if filename == files[i]:
                print(contents[i])
                break
        else:
            print("File not found")

while selection.upper() != "X":
    print('''Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:''')
    selection = input()
    options(selection)

print("Goodbye!")
    
    
    
    