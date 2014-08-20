cost = eval(input("Enter the cost (in cents):\n"))
if cost!=0:
    useracc =0
    depo =0
    while useracc < cost:
        depo = eval(input("Deposit a coin or note (in cents):\n"))
        useracc+=depo
   
    change = useracc-cost
    if change!=0:
        print("Your change is:")
        num1d=change//100
        if num1d!=0:
            print(num1d,'x $1')
        change = change - num1d*100
        num25c=change//25
        if num25c!=0:
            print(num25c,'x 25c')
        change = change - num25c*25
        num10c=change//10
        if num10c!=0:
            print(num10c,'x 10c')    
        change = change - num10c*10
        num5c=change//5
        if num5c!=0:
            print(num5c,'x 5c')
        change = change - num5c*5
        if change>0:
            print (change, 'x 1c')
