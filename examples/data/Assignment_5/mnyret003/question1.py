# A program to simulate a simple BBS
# Retselisitsoe Monyake
# 16 April 2014

def main():
    message="no message yet"
    while True:
        menu=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
        menu = menu.upper()
        if menu=="E":
            message=input("Enter the message:\n")
        elif menu=="V":
            print("The message is: "+message)
        elif menu=="L":
            print("List of files: 42.txt, 1015.txt")
        elif menu=="D":
            file=input("Enter the filename:\n")
            if file=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file=="1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print("File not found")
        elif menu=="X":
            print("Goodbye!")
            break
        
main()