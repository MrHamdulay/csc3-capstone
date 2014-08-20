h=eval(input("Enter the height of the triangle:\n"))
x=0
for i in range(1,h+1,1):
    x+=1
    gap=h-x
    y=2*x-1
    print(" "*gap,"*"*y,sep="")