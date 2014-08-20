#Question 1, Assignment 5
#Duncan Saffy
#14-04-2014
n=""
mes=""
while n != "x":
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    n=input("Enter your selection:\n")

    if n == "E" or n=="e":
        mes= input("Enter the message:\n")
   
    
    elif n == "V" or n== "v":
        if len(mes)<=2:
            print("The message is: no message yet")
        else:
            print("The message is:",mes)
    
    elif n== "L" or n== "l":
        #listt=input("List of files:")
        print("List of files: 42.txt, 1015.txt")
        
    elif n== "d" or n=="D":
        disp= input("Enter the filename:\n")
        if disp== "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif disp == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")

        
    
print("Goodbye!")