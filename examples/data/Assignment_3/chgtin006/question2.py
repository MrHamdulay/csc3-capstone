height=eval(input("Enter the height of the triangle:\n"))
height=height*2
gap=height//2
gap=gap-1
for i in range(1,height+1,2):
    print(" "*gap,end="")
    print("*"*(i))
    gap=gap-1