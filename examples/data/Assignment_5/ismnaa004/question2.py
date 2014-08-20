def vendor():
    cost=eval(input('Enter the cost (in cents):\n'))
    deposit=eval(input('Deposit a coin or note (in cents):\n'))
    total=0
    while not deposit>=cost:
        deposit=eval(input('Deposit a coin or note (in cents):\n'))
        total=deposit+total
        change=total-cost
    