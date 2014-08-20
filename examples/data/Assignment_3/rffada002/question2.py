height = eval(input("Enter the height of the triangle:\n"))
x=height-1

for i in range(1,height+1):
    print(" "*x,sep='',end='')
    print("*"*((i*2)-1),sep='')
    x=x-1