def isotri():
    x=eval(input("Enter the height of the triangle:\n"))
    if x%2==0:
        gap=x//3
        gap=3*gap 
        for i in range(0,2*x,2):
            print(' '*gap,end='')
            print('*'*(i+1))
            gap=gap-1        
        
    else:
        gap=x//2
        gap=2*gap 
        for i in range(0,2*x,2):
            print(' '*gap,end='')
            print('*'*(i+1))
            gap=gap-1
isotri()
