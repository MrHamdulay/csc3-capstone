x=eval(input("Enter the height of the triangle:\n"))
width=2*x-1
for i in range(1,x+1):
    print(" "*(x-1)+"*"*(width-2*(x-1)),sep="")
    x=x-1
    

