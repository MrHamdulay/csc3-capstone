height = eval(input("Enter the height of the triangle:\n"))
spaces = height - 1
for i in range(height):
    x = (i * 2)*'*'+'*'
    print(' '*spaces,x,sep='')
    spaces=spaces-1