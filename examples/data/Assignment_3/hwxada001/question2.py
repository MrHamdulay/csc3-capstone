h = eval(input("Enter the height of the triangle:"))
for i in range(0,h,1):
    for k in range(h-i):
        print(" ",end='')
    for j in range(i*2-1):
        print("*",end='')
    print()
print("*"*((h*2)-1))