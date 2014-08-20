height = eval(input('Enter the height of the triangle:\n'))

width = (height * 2) - 1

for k in range(1, height + 1):
    tri = '*' * ((2 * k) - 1)
    tri = ("{0:^"+str(width)+"}").format(tri)
    print(tri)