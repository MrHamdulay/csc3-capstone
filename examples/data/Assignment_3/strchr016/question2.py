x=eval(input("Enter the height of the triangle:\n"))
gap=x-1
for i in range(1,2*x,2):
        print(gap*" ",end="")
        print(i*"*")
        gap-=1