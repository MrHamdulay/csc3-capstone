"""program to simulate a simple BBS
Dumisani J Nyathi
16-04-2014"""

def main():
    #to get the program started
    #create variables
    E=("(E)nter a message")
    V="(V)iew message"
    l="(L)ist files"
    d="(D)isplay file"
    X="e(X)it"
    z=""
    y=""#place holder
    i=0
    
    
    #create a loop which will iterate as long as input supplied is not x
    while z != "X" :
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        x=input("Enter your selection:\n")    
        z=x.upper()#to account for lower case supplied input
        if z=="E":
            y=input("Enter the message:\n")
        elif z=="V":
            if y=="":
                print("The message is: no message yet")
            else: 
                print("The message is:",y)
        elif z=="L":
            print("List of files: 42.txt, 1015.txt")
        elif z=="D":
            j=input("Enter the filename:\n")
            if j=='42.txt':
                print("The meaning of life is blah blah blah ...")
            elif j=='1015.txt':
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            elif j=='1016.txt':
                print("File not found")
            else:
                print("File not found")        
    print("Goodbye!")

main()