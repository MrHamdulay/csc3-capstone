n=eval(input("Enter the height of the triangle:\n"))
x=2*n
gap=x//2-1
for i in range(1 ,x, 2):
    print(" "*gap, "*"*i, sep="")
    gap-=1