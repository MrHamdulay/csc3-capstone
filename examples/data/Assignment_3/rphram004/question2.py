x = eval(input("Enter the height of the triangle:\n"))
y = x-1
space = x//2
for i in range(1,(y*2)+2,2):
        print(' '*(x-1),'*'*i, sep='')
        x=x-1
        
