#A program simulating a simple BBS system used to share files and messages
#created by:Jenna Lake
#Date: 15/4/2014

def bbs():
    d=True
    c=1 # default variable, showing that so message has been entered
    mes="" #empty string to attactch the message to
    while d:# loop, such that the menu displays at the end of each action
        print("Welcome to UCT BBS\n","MENU\n","(E)nter a message\n","(V)iew message\n","(L)ist files\n","(D)isplay file\n","e(X)it", sep="")
        selection=input("Enter your selection:\n")
        if selection=='E' or selection=='e':
            mes+=input("Enter the message:\n")
            c=2 # variable shows python that a message has been entered
        if selection=='V' or selection=='v':
            if c==1:
                print("The message is: no message yet")            
            else:
                print("The message is:", mes, sep=" ")
        if selection=='L' or selection=='l':
            print("List of files: 42.txt, 1015.txt")
        if selection=='D' or selection=='d':
            x=input("Enter the filename:\n")
            if x=='42.txt':
                print("The meaning of life is blah blah blah ...")
            elif x=='1015.txt':
                print("Computer Science class notes ... simplified\n", "Do all work\n","Pass course\n","Be happy", sep="")
            else:
                print("File not found")
        if selection=='X' or selection=='x':
            print("Goodbye!")
            d=False #allows loop to break 
            break
    if mes:
        return mes #store inputed message so that it may be referenced in a later loop
bbs()