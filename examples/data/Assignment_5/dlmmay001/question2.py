def vending_machine():
    depo = []
    cost = eval(input("Enter the cost (in cents):\n"))
    #deposit = eval(input("Deposit a coin or note (in cents):\n"))
   # depo.append(deposit)
   # depo1 = sum(depo)
    deposit = ''
    depo1 = 0
    while depo1 < cost:
        deposit = eval(input("Deposit a coin or note (in cents):\n"))
        depo.append(deposit)
        depo1 = sum(depo)

    change = depo1 - cost 
    dol = change//100
    left = change%100
    if change > 0:
        print('Your change is:')
    if dol > 0:
        print(dol,'x $1')
    LIST = [25,10,5,1]
    
    left1 = left    
    for i in LIST:
        left = left//i
        if left1%i!=0:
            print(left,' x ',i,'c',sep='')
            left = left1 - (i*left)
            left1 = left 
        if left1%i == 0:
            print(left,' x ',i,'c',sep='')
            break

       # left = left1-i
       # left1 -= left 
        #if left1%i==0:
           # break
        #if left%i !=0:
           ## break

vending_machine()