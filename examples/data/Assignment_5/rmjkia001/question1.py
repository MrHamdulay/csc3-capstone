"""UCT BBS - Kiara Ramjith - 2014"""
op= input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")#ask for input
mes=""#create a variable
while(op!= "X" or op !="x"): #while the input is not x, rerun
    if(op=="E" or op=="e"):#test
        mes = input("Enter the message:\n")
    elif(op =="V" or op== "v"):
        if (mes==""):
            print("The message is: no message yet")
        else:
            print("The message is: "+mes)
    elif(op=="L" or op=="l"):
        print("List of files: 42.txt, 1015.txt")
    elif(op=="D" or op=="d"):
        fn=input("Enter the filename:\n")
        if(fn=="42.txt"):
            print("The meaning of life is blah blah blah ...")
        elif(fn=="1015.txt"):
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    elif(op=="x" or op=="X"):#what happens when x is input
        break
    op= input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")#re ask for oprtion
print("Goodbye!")
            