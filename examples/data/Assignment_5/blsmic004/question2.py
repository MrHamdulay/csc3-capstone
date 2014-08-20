''' Vending machine simulation to calculate change
Michele Balestra BLSMIC004
14 April 2014'''

cost = eval(input("Enter the cost (in cents):\n"))

deposit = 0
while deposit<cost:
    deposit = deposit + eval(input("Deposit a coin or note (in cents):\n"))

change = deposit - cost
dollar,quarter,ten,five,one = '','','','',''
if change!=0:
    print("Your change is:")
while True:
    if change==0:
        break
    elif change-100>=0:
        print(str(change//100) + " x $1")
        change = change-(change//100*100)
    elif change-25>=0:
        print(str(change//25) + " x 25c")
        change = change-(change//25*25)
    elif change-10>=0:
        print(str(change//10) + " x 10c")
        change = change-(change//10*10)
    elif change-5>=0:
        print(str(change//5) + " x 5c")
        change = change-(change//5*5)
    elif change-1>=0:
        print(str(change//1) + " x 1c")
        change = change-(change//1*1)
    else: break