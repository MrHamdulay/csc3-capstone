height = eval(input("Enter the height of the triangle:\n"))
gap = height - 1
for i in range(height):
    x = (i * 2)*'*'+'*'
    print(' '*gap,x,sep='')
    gap=gap-1