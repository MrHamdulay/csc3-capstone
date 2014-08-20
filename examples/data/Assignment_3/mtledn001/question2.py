#Print a cool triangle
h = eval(input('Enter the height of the triangle:\n'))
gap = h-1
for i in range(1,h*2+1,2):
    if gap==0:
        print('*'*i)  
    else: print(' '*(gap-1),'*'*i)
    gap-=1;
    