x=eval(input("Enter the height of the triangle:\n"))

y=x-1
z=1

for i in range(x):
    print(" "*y,"*"*z,sep="")
    y=y-1
    z=z+2
  