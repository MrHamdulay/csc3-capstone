x= eval(input("Enter the height of the triangle:\n"))
y=1
z=0
t=x-1
u=0
for i in range(x):
    print(" "*(t-u),"*"*y,sep="")
    y+=2
    u+=1