H=eval(input("Enter the height of the triangle:\n"))
gap=H-1
n=1
for i in range(H):
    print(" "*gap,end="")
    print("*"*n)
    gap=gap-1
    n=n+2
