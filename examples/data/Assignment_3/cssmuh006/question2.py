h=eval(input("Enter the height of the triangle:\n"))
i=1
while h!=0:
    print(" "*(h-1),"*"*i,sep="")
    i+=2
    h+=-1