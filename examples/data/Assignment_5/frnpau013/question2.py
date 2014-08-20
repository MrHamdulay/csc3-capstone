cost = eval(input("Enter the cost (in cents):\n"))
deposited = 0

while deposited < cost:
    deposited += eval(input("Deposit a coin or note (in cents):\n"))
    
change = deposited - cost

if change == 0:
    print("")
else:
    print("Your change is:")
    dollar_number = change//100
    quarter_number = (change - (dollar_number*100))//25
    tenth_number = (change - (dollar_number*100) - (quarter_number*25))//10
    twentieth_number = (change - (dollar_number*100) - (quarter_number*25) - (tenth_number*10))//5
    hundreth_number = (change - (dollar_number*100) - (quarter_number*25) - (tenth_number*10) - (twentieth_number*5))
    
    denominations = ['$1', '25c', '10c', '5c', '1c']
    
    count = 0
    for i in [dollar_number, quarter_number, tenth_number, twentieth_number, hundreth_number]:
        if i == 0:
            count += 1
            continue
        else:
            print(i, "x", denominations[count])
            count += 1
              