def triangle():
#input
    height = eval(input("Enter the height of the triangle: \n"))
    count = 1
    x = height
#processing -- output
    for i in range(0,height):
   
        print(' '*(x-1),end='')
        print('*'*(count))
        x+=-1
        count+=2

triangle()