height=eval(input("Enter the height of the triangle:\n"))
x=1
y=height-1
for i in range(1,height+1):
    print(" "*y,end="")
    print("*"*x,)
    y=y-1
    x=x+2