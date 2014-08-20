#Kalind Ramnarayan


x=eval(input("Enter the height of the triangle:\n"))
gap=(x-1)
for i in range(x):
    print(" "*gap,"*"*(2*i+1), sep="")
    gap=gap-1