"""vending machine simulator
Vahin Gounden
15 April 2014"""

#enter the cost
cost = eval(input("Enter the cost (in cents):\n"))

#check if item is free
if cost != 0:
    #check is user deposited enough cash
    coin = eval(input("Deposit a coin or note (in cents):\n"))
    total = coin
    while total < cost:
        coin2 = eval(input("Deposit a coin or note (in cents):\n"))
        total = coin + coin2
        
    #find change if there is
    change = total - cost
    d = change//100
    c25 = (change - d * 100)//25
    c10 = (change - (d * 100 + c25 * 25))//10
    c5 = (change - (d * 100 + c25 * 25 + c10 *10))//5
    c1 = (change - (d * 100 + c25 * 25 + c10 *10 + c5 * 5))
    if change != 0 and cost != 50:
        print("Your change is:")
        if d != 0:
            print(d,"x $1")
        if d *100 != change:
            print(c25,"x 25c")
        if d * 100 + c25 * 25 != change:
            print(c10,"x 10c")
        if d * 100 + c25 * 25 + c10 *10 != change:
            print(c5,"x 5c")
        if d * 100 + c25 * 25 + c10 *10 + c5 * 5 != change:
            print(c1,"x 1c")
    if cost == 50:
        print("Your change is:")
        print("1 x 25c")
        print("2 x 10c")