"""program to simulate a simple BBS
Nosipho Khumalo
11 April 2014"""

def main():
    message = ""
    while True:
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        option = input("Enter your selection: \n")
        default = "no message yet"
        if option in ("E","e"):
            message = input("Enter the message: \n")
        elif option in ("V","v"):
            if message == "":
                print("The message is:", default)
            else: print("The message is:", message)
        elif option in ("L","l"):
            print("List of files: 42.txt, 1015.txt")
        elif option in ("D","d"):
            filename = input("Enter the filename: \n")
            if filename == "42.txt":
                print("The meaning of life is blah blah blah ...")
            elif filename == "1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            elif filename not in ("1015.txt", "42.txt"):
                print("File not found")
        elif option in ("x", "X"):
            print("Goodbye!")
            break
main()