height= eval(input("Enter the height of the triangle:\n"))
for x in range (1,height+1):
    for y in range (height-x):
        print(" ",end="")
    for z in range ((2*x)-1):
        print("*", end="")
    print("")