infile=open("42.txt", "w")
print("The meaning of life is blah blah blah ...", file=infile)
infile.close()
infile=open("1015.txt", "w")
print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy", file=infile)
infile.close()
infile = open("m.txt", "w")
infile.close()
outfile=open("42.txt", "r")
file1=outfile.read()
outfile.close()
outfile=open("1015.txt", "r")
file2=outfile.read()
outfile.close()
outfile=open("m.txt", "r")
file3=outfile.read()
outfile.close()
for i in range(20):
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    c=input("Enter your selection:\n")
    c=c.upper()
    if c == "E":
        infile=open("m.txt", "w")
        mes=input("Enter the message:\n")
        print(mes, file=infile)
        file3=mes
        infile.close()
    elif c=="V":
        if file3 == "":
            print("The message is: no message yet")
        else:
            print("The message is:", file3)
    elif c == "L":
        print("List of files: 42.txt, 1015.txt")
    elif c == "D":
        file = input("Enter the filename:\n")
        if file == "42.txt":
            print(file1, end ="")
        elif file =="1015.txt":
            print(file2, end="")
        else:
            print("File not found")
    elif c == "X":
        print("Goodbye!")
        break
        
            
   
    
    
