



import math
#get function from user
f= input('Enter a function f(x):\n')


#print function on graph
for y in range (10,-11, -1):
    for x in range(-10,11):
        xr = x/10
        yr = -y/10
        i = '('+str(x)+')'
        r = f.replace('x', i)
        r = eval(r)
        if y == round(r):
            print('o', end='')        
        else:
            if  xr== 0 and yr == 0:
                print('+', end='')
            elif yr == 0:
                print('-', end='')
            elif xr == 0:
                print('|', end='')
                   
            else:
                print(' ', end='')
    print()    
