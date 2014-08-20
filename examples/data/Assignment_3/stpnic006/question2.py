x=eval(input("Enter the height of the triangle:\n"))
def shape(x):
    gap=(x-1)
    for i in range(0,x*2-1,2):
        print(" "*gap,end="")
        print("*"*(1+i))
        gap-=1
        
shape(x)