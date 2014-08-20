x = eval(input("Enter the height of the triangle:\n"))
k=1
spaces = x-1

while k<=2*x:
    print(" "*spaces,"*"*k,sep="")
    spaces -= 1
    k += 2


