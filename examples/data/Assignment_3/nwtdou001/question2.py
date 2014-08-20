h = eval(input("Enter the height of the triangle:\n"))
for i in range(h,0,-1):
    print(' '*(i-1),'*'*((h-i+1)*2-1),sep='')