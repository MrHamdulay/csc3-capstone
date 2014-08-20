""" bbs uct
danson masuka
15 April 2014"""

E=("(E)nter a message")
V="(V)iew message"
l="(L)ist files"
d="(D)isplay file"
X="e(X)it"
answer=""
e1="" 
i=0
m="42.txt"
n="1015.txt"

# the loop 
while answer != "x" :
    print ("Welcome to UCT BBS")
    print ("MENU")
    print(E,V,l,d,X, sep="\n")
    answer=input("Enter your selection:\n") 
    if answer=="E" or answer=="e":
        e1=input("Enter the message:\n")
    elif answer=="V" or answer=="v":
        if e1=="":
            print("The message is: no message yet")
        else: 
            print("The message is:",e1)
    elif answer=="l" or answer=="L":
        print("List of files: 42.txt, 1015.txt")
    elif answer=="d" or answer=="D":
        a=input("Enter the filename:\n")
        if a==m:
            print("The meaning of life is blah blah blah ...")
        elif a==n:
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print('Pass course')
            print('Be happy')
        else :print("File not found")
print("Goodbye!")
        
    