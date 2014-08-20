height=eval(input("Enter the height of the triangle:""\n"))
for i in range(height+1):
    if i!=0:
        print(" "*(height-i),"*"*(2*i-1),sep="")
    else:
        continue
