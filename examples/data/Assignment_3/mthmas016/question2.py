x=eval(input("Enter the height of the triangle:""\n"))
for i in range(x):
    m="*"
    print(" "*(x-i-1),m*(2*i+1),sep="")
