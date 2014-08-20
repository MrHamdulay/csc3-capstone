x=eval(input("Enter the height of the triangle:\n"))
z=1
y=(x+(x-1))


for i in range(0,x):
    a=int((y-z)/2)
    print(" "*a,"*"*z," "*a, sep="")
    z+=2
    