x=input("Enter the height of the triangle:"'\n')
gap=eval(x)-1
for i in range(0,eval(x)+(eval(x)-1),2):
        print(' '*gap,end='')
        print('*'*(i+1))
        gap-=1