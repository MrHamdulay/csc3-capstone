x=eval(input("Enter the height of the triangle:\n"))
space=x-1
star=1
for i in range(0,x):
    print(" "*space,end="")
    print("*"*star)
    space=space-1
    star=star+2

