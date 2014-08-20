inputs=input("Enter the input filename:\n")
output=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))
f=open(inputs,"r")
lines=f.readlines()
f.close()
for line in range(len(lines)):
    lines[line]=lines[line][:-1]
x=" ".join(lines)
letters=0
templetters=0
outputlines=len(x)//width
for h in range(0,outputlines+1):
    letters+=templetters
    templetters=0
    for i in range(width*(h+1)-letters,width*h-letters-1,-1):
        if i>=len(x):
            continue
        elif i==len(x)-1:
            if h>0:
                g=open(output,"a")
                print(x[width*h-letters+1:i+1], file=g)
                g.close()
                break
            else: 
                g=open(output,"a")
                print(x[width*h-letters:i+1], file=g)
                g.close()
                break
        elif x[i]==" ":
            if x[width*h-letters]==" ":
                g=open(output,"a")
                print(x[width*h-letters+1:i], file=g)
                g.close()
                break
            else:
                g=open(output,"a")
                print(x[width*h-letters:i], file=g)
                g.close()       
                break
        else: 
            templetters+=1
        