x = input("Enter the input filename:\n")
y = input("Enter the output filename:\n")
z = eval(input("Enter the line width:\n"))

openfile = open(x, 'r')
readline = openfile.read()
openfile.close()


separate = readline.split("\n\n")
openfile2 = open(y, "w")
for i in separate:
    i = i.replace("\n"," ")
    i = i.split(" ") 
    add=-1
    for a in i:
        add+=len(a)+1
        if add <= z:
            print(a,file=openfile2,end= " ")
        else:
            print(file=openfile2)
            print(a,file=openfile2,end=" ")
            add = len(a)
    print(file=openfile2)
    print(file=openfile2)
openfile2.close()
    

