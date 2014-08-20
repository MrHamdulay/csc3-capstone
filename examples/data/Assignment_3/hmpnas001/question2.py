def triangle():
    h=eval(input('Enter the height of the triangle:\n'))
    gap=(2*h)//2
    for i in range(0,2*h,2):
        gap=gap-1
        print(' '*gap,end='')
        print('*'*(i+1))
             
triangle()           