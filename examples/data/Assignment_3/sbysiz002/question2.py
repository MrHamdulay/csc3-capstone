h=eval(input("Enter the height of the triangle:\n"))
gap=h-1
add=1
for i in range(h):
    print(" "*gap,"*"*add, sep="")
    add=add+2
    gap=gap-1
    