m=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
f=eval(input("Enter the frame thickness:\n"))

y=len(m)+2*f
z=len(m)+2
gap=0
for i in range(y, z-2, -2):
    print("|"*gap,"+","-"*i,"+", "|"*gap, sep="")
    gap+=1
    
for j in range(r):
    print("|"* f, m.center (y-2*f), "|"*f)
    
gap=f-1

for i in range (z, y+1, 2):
    print("|"*gap, "+", "-"*i, "+", "|"*gap, sep="")
    gap-=1

       