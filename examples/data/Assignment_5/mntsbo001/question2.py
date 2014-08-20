a = eval(input("Enter the cost (in cents):\n"))
b = eval(input("Deposit a coin or note (in cents):\n"))
while a>b:
    c = eval(input("Deposit a coin or note (in cents):\n"))
    b = b+c
d = b-a
while d!=0:
    print('Your change is:')
    while d>=100:
        e = d//100
        d = d-e*100
        print(e,'x $1')
    while d>=25:
        f = d//25
        d = d-f*25
        print(f,'x 25c')
    while d>=10:
        g = d//10
        d = d-g*10
        print(g,'x 10c')
    while d>=5:
        h = d//5
        d = d-h*5
        print(h,'x 5c')
    while d>=1:
        i = d
        d = d-i
        print(i,'x 1c')
        
        
        
        