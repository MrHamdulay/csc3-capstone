h=eval(input("Enter the height of the triangle:\n"))
c=h-1
z=1
for i in range(h):
    for s in range(c):
        print(" ",end="")
    print("*"*z)
    z+=2
    c-=1
    