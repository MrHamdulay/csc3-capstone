
x=eval(input("Enter the height of the triangle:""\n"))
gap=x-1
y=1
for i in range(x):
    print(" "*gap,end="")
    print("*"*y)
    gap-=1
    y=y+2