A=eval(input("Enter the height of the triangle:\n"))
for i in range (A+1):
    if i!=0:
        print(" "*(A-i),"*"*(2*i-1),sep="")
    else:
            continue