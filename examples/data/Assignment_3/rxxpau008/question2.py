def triangle (height):
    height = height+height-1
    space=height//2
    for i in range(0,height,2):
        print(' '*space,end='')
        print('*'*(i+1))
        space=space-1
    length = height//4
    space=height//2

h = eval(input("Enter the height of the triangle:\n"))
triangle(h)