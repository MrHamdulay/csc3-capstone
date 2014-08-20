def tri():
    x=eval(input("Enter the height of the triangle:\n"))
    k=1
    gap=x-1
    for i in range(0,x):
        print(' '*gap,end='')
        print('*'*k)
        gap-=1
        k+=2
tri()