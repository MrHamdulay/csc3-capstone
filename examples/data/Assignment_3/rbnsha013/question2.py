print("Enter the height of the triangle:")
h = eval(input())
gap = h - 1
for i in range(0,2*h,2):
    print(" "*gap+"*"*(i+1))
    gap = gap - 1