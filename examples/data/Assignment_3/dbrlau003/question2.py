x=eval(input("Enter the height of the triangle:\n"))
y=1
for i in range(x):
    print(" "*(x-i-1),end="")
    print(y*'*',end="")
    print(" "*(x-i-1))
    y=y+2