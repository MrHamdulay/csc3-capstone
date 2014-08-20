x=eval(input("Enter the height of the triangle:\n"))
b=1
a=x-1
space=" "*a
for i in range(x):
    print(space, "*"*b, sep="")
    a-=1
    b+=2
    space=" "*a
   
