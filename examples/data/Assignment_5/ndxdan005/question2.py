cost=eval(input("Enter the cost (in cents):\n"))

cash=0

while cash<cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    cash=cash+deposit
    
change=cash-cost
dollar=change//100
quarter=(change%100)//25
tenner=(change%25)//10
fiver=(change%10)//5
cent=(change%5)

if change>0:
    print("Your change is:")

if change>=100:
    print(dollar, "x $1")
    if quarter>0:
        print(quarter, "x 25c")
    if tenner>0:
        print(tenner, "x 10c")
    if fiver>0:
        print(fiver, "x 5c")
    if cent>0:
        print(cent, "x 1c")
    
elif change>=25:
    print(quarter, "x 25c")
    if tenner>0:
        print(tenner, "x 10c")
    if fiver>0:
        print(fiver, "x 5c")
    if cent>0:
        print(cent, "x 1c")
    
elif change>=10:
    print(tenner, "x 10c")
    if fiver>0:
        print(fiver, "x 5c")
    if cent>0:
        print(cent, "x 1c")
    
elif change>=5:
    print(fiver, "x 5c")
    if cent>0:
        print(cent, "x 1c")
    
elif change>=5:
    print(cent, "x 1c")