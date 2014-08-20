list=[100,25,10,5,1]
x=eval(input("Enter the cost (in cents):\n"))
y=0

while y<x:
    z=eval(input('Deposit a coin or note (in cents):\n'))
    y+=z
if y>x:
    e=(y-x)
    print('Your change is:')
    for i in list:
        if i==100 and e//i>0:
            print(e//i,' x $',1,sep='')
            e=e%i
        elif e//i>0:
            print(e//i,' x ',i,'c',sep='')
            e=e%i
        else:
            continue
            
        

    

    
    