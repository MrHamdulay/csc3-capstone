""" Programme to calculate change
Adam Kaliski
CSC1015 Assignment 5 """
onedoll=0
twofive=0
ten=0
five=0
one=0
cost = eval(input('Enter the cost (in cents):\n'))
if cost > 0:
    tender=eval(input('Deposit a coin or note (in cents):\n'))
    while tender<cost:
        tender += eval(input('Deposit a coin or note (in cents):\n'))
    change = tender - cost
    if change>0:
        while change >= 100:
            onedoll += 1
            change-=100
        while change >= 25:
            twofive += 1
            change -= 25
        while change >= 10:
            ten += 1
            change -= 10
        while change >= 5:
            five +=1
            change -= 5
        while change >= 1:
            one += 1
            change -= 1
        
        print('Your change is:')
        if onedoll != 0:
            print(onedoll,'x $1')
        if twofive != 0:
            print(twofive,'x 25c')    
        if ten != 0:
            print(ten,'x 10c')
        if five != 0:
            print(five,'x 5c')            
        if one != 0:
            print(one,'x 1c')                