b=eval(input("Enter the height of the triangle:\n"))
a=b-1
d=1

for i in range(b):
    print(" "*a,"*"*d,sep="")
    a=a-1
    d=d+2