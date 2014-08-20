# programe that graphically illustrates functions 
# Aaron Daniels
# 15 April 2014

x=eval(input('Enter the cost (in cents):\n'))
k=0
while k<x:
    i=eval(input('Deposit a coin or note (in cents):\n'))
    k+=i
if k==x:
    print()
elif k>x:
    d=k-x
    p=d//100
    q=d%100
    e=q//25
    w=q%25
    r=w//10
    s=w%10
    f=s//5
    g=s%5
    
    print('Your change is:')
    if p!=0:    
        print(p,'x $1')
    if e!=0:  
        print(e,'x 25c')
    if r!=0:  
        print(r,'x 10c')
    if f!=0:  
        print(f,'x 5c')
    if g!=0:  
        print(g,'x 1c')
    





