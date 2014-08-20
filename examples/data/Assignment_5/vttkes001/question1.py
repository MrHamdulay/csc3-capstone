""" Public Bulletin Board System
Keshin Vittee
16 April 2014 """
mess = "no message yet"

while True:
    print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it",sep="\n")
    ans = input("Enter your selection:\n")
    ans = ans.lower()
    if ans == 'e':
        mess = input("Enter the message:\n")
    elif ans == 'v':
        print("The message is:",mess)
    elif ans == 'l':
        print("List of files: 42.txt, 1015.txt")
    elif ans == 'd':
        fname = input("Enter the filename:\n")
        if fname == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif fname == "1015.txt":
            print("Computer Science class notes ... simplified","Do all work","Pass course","Be happy",sep="\n")
        else:
            print("File not found")
    elif ans == 'x':
        print("Goodbye!")
        break
    