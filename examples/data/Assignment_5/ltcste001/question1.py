#Stephanie Latchmanan(LTCSTE001)
#BBS system(Assignment 5 Question 1)
#16 April 2014
def sel1():
    print("The meaning of life is blah blah blah ...") #input a value for 42.txt

def sel2():
    print("Computer Science class notes ... simplified") #input a value for 1015.txt
    print("Do all work")
    print("Pass course")
    print("Be happy")
msg="no message yet"
sel=""
while sel != 'X' or sel != 'x':       #run menu until x is pressed
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    sel=input("Enter your selection:\n")
    if sel == 'E' or sel =='e':
        msg=input("Enter the message:\n")      #input a message
        continue
    if sel == 'V' or sel == 'v':
        print("The message is:", msg)
        continue
    if sel == 'L' or sel =='l':
        print("List of files: 42.txt, 1015.txt")
        continue
    if sel == 'D' or sel == 'd':
        filename=input("Enter the filename:\n")
        if filename == '42.txt':
            sel1()
            continue
        if filename == '1015.txt':
            sel2()
            continue
        else:
            print("File not found")
        continue
    if sel == 'x' or sel == 'X':
        break

print("Goodbye!")