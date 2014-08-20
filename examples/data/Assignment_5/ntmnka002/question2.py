cost = eval(input('Enter the cost (in cents):\n'))
dep = 0
total = 0

if cost != 0:

    while total < cost:
        dep = eval(input('Deposit a coin or note (in cents):\n'))
        total += dep
        
    dif = total - cost
    
    if dif != 0:
    
        print('Your change is:')
        
        one =  dif//100
        if one != 0:
            print(one, ' x $1', sep = '')
            
        dif -= (one * 100)
            
        twentyf =  dif//25
        if twentyf != 0:
            print(twentyf, ' x 25c', sep = '')
            
        dif -= (twentyf * 25)
                
        ten =  dif//10
        if ten != 0:
            print(ten, ' x 10c', sep = '')
            
        dif -= (ten * 10)
        
        five =  dif//5
        if five != 0:
            print(five, ' x 5c', sep = '')
            
        dif -= (five * 5)
        
        one =  dif//1
        if one != 0:
            print(one, ' x 1c', sep = '')
            
        dif -= (one * 1)