#Assignment 5, Question 2
#Avreyna Kistensamy
#14 April 2014

cost = eval(input("Enter the cost (in cents):\n"))
if cost != 0:
    cash = eval(input("Deposit a coin or note (in cents):\n"))
    while cash < cost:
        more_cash = eval(input("Deposit a coin or note (in cents):\n"))
        cash= cash + more_cash
        if cash==cost: break
    else:
        change = cash-cost
        print("Your change is:")
        if change >= 100:
            a= change//100
            print(a, "x $1")
            change = change - a*100
        if 25 <= change <100:
            b=change//25
            print(b, "x 25c")
            change = change - b*25
        if 10 <= change < 25:
            c=change//10
            print(c, "x 10c")
            change = change - c*10
        if 5<= change <10:
            d=change//5
            print(d, "x 5c")
            change = change - d*5
        if 1<= change < 5:
            print(change, "x 1c")
            
        
            
        
