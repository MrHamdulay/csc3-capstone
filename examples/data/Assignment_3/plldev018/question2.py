a=eval(input("Enter the height of the triangle:\n"))
b=1
for i in range(0,a,1):
    print(" "*(a-1),end="")
    print("*"*b,end="")
    print(" "*a)
    a=a-1
    b=b+2