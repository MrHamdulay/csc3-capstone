def vending_Machine():
    cost = eval(input("Enter the cost:\n"))
    x = 0
    while x < cost:
        deposit = eval(input("Enter the deposit:\n"))
        x += deposit
    change = x - cost
    d = [100,25,5,1]
    for i in d:
        if change % i != 0:
            y = (change//i)
            if i == 100:
                print("Your change is:\n",y,"x $1")
            else:
                print("jgj")
            change = change % i
        
            


vending_Machine()