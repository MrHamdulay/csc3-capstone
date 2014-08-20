"""Simple Bulletin Board System
Tafadzwa Moyo
16 April 2014"""

#Defining variables
msg="no message yet"
files=[["42.txt", "The meaning of life is blah blah blah ..."],["1015.txt", "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"]]

#Prints menu
print("Welcome to UCT BBS", "MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it", sep="\n")

#User input
cmd=input("Enter your selection:\n").lower()[0] #allows upper and lower case input, the first letter has to match an option
#Procressing command
while cmd!='x':
    if cmd == "e":
        msg=input("Enter the message:\n")
    elif cmd=="v":
        print("The message is:", msg)
    elif cmd=="l":
        print("List of files:",files[0][0]+", "+files[1][0])
    elif cmd=="d":
        cmd = input("Enter the filename:\n") 
        if cmd == files[0][0]:
            print(files[0][1])
        elif  cmd == files[1][0]:
            print(files[1][1])
        else: print("File not found")
    print("Welcome to UCT BBS", "MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it", sep="\n")
    cmd=input("Enter your selection:\n").lower()
#Print God when while terminates
print("Goodbye!")
            