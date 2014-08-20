import math
fn=input("Enter a function f(x):\n")
x=0
for i in range(10,-11,-1):
    for n in range(-10,11,1):
        x=n
        y=round(eval(fn))    
        if y==i:
            print('o', end='')
        if n==0 and i==0 and y!=i:
            print('+', end='')
        if i==0 and n!=0 and y!=i:
            print('-',end='')
        if n==0 and i!=0 and y!=i:
            print('|', end='')          
        if n!=0 and i!=0 and y!=i:
            print(' ', end='')
    print()
              