h=eval(input("Enter the height of the triangle:\n"))
gap=(h-1)
for i in range(h):
    print(" "*gap+"*"*(i*2+1))
    gap=gap-1