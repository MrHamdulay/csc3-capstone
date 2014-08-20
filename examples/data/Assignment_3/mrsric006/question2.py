def a():
    par1= 2*(eval(input('Enter the height of the triangle:\n')))
    gap=par1//2 
    for i in range(0,par1,2):
        print(' '*(gap-1),end='') 
        print('*'*(i+1))
        gap=gap-1 
        
a()

