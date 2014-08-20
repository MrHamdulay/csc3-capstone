h=eval(input("Enter the height of the triangle:\n"))
x=1
y=h-1 #how many spaces
for i in range(h):
    print(" "*y, "*"*x,sep="")
    #print("*"*x)
    x+=2
    y-=1
    

