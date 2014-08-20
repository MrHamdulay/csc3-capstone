x=eval(input("Enter the height of the triangle:""\n"))
for i in range(x+1):
    if i!=0:
        print(" "*(x-i),"*"*(2*i-1),sep="")
    else:
        continue