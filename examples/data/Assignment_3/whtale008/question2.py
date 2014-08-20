h = eval(input("Enter the height of the triangle:"))
w = h
for i in range(h+1):
    print(' '*(w),'*'*(2*i - 1),sep='')
    w = w-1