t=eval(input("Enter a number:"))
gap=(t+t-1)//2
b=1
for i in range(0,t):
    print(" "*gap,end=" ")
    gap-=1
    print("*"*(2*i+b))