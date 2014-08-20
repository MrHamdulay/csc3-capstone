height = eval(input("Enter the height of the triangle:\n"))
count = 1
for i in range(height,0,-1):
    print(" "*(i-1)+"*"*count)
    count = count+2