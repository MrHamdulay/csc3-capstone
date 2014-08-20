x = eval (input ('Enter the height of the triangle:\n'))
for i in range (1, x+1):
    gap = ' ' * (x-i)
    print (gap, '*' * (2*i-1), gap, sep='')