print("Enter the height of the triangle:")
h=eval(input())*2
gap=h//2
for g in range(1,h,2):
    print(" "*gap,end="")
    print("*"*(g))
    gap-=1