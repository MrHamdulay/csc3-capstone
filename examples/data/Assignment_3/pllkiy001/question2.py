h=eval(input("Enter the height of the triangle: \n"))
for i in range(h+1):
    if i!=0:
        print(" "*(h-i),"*"*(2*i-1),sep="")
    else:
            continue
