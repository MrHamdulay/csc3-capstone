height=eval(input("Enter the height of the triangle:\n"))
gap=height-1
count=1
for i in range(height):
    print(' '*gap,end='')
    print("*"*(i+count))
    gap=gap-1
    count=count+1
