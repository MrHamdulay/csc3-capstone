'''a vending machine program that takes in a cost and deposited money,compare it and prints out change if there is some'''

#ask for cost
cost = eval(input("Enter the cost (in cents):\n"))
#ask for deposit
deposit = eval(input("Deposit a coin or note (in cents):\n"))

#ask deposit till cost <= total deposit
while cost > deposit:
    deposit=deposit + eval(input("Deposit a coin or note (in cents):\n"))
    
change = deposit-cost

printings=[]

if change//100 > 0:
    dollars="{} x $1".format(change//100)
    printings.append(dollars)

change=change-(change//100)*100

if change//25 > 0:
    quaters ="{} x 25c".format(change//25)
    printings.append(quaters)
    
change=change-(change//25)*25

if change//10 > 0:
    ten_cents="{} x 10c".format(change//10)
    printings.append(ten_cents)

change=change-(change//10)*10

if change//5 > 0:
    five_cents="{} x 5c".format(change//5)
    printings.append(five_cents)

change=change-(change//5)*5

if change//1 > 0:
    one_cents="{} x 1c".format(change//1)
    printings.append(one_cents)

print("Your change is:")
for i in printings:
    print(i)