#assignment 6.2
coins = 0
cost = eval(input("Enter the cost (in cents):\n"))
while cost > coins:
    coins = coins + eval(input("Deposit a coin or note (in cents):\n"))
change = coins - cost
if change != 0:
    print("Your change is:")
k = 100
for k in [100,25,10,5,1]:
    count = 0
    while change - k >= 0:
        change = change - k
        count += 1
    if count > 0:
        if k == 100:
            print(str(count) + " x $1")
        else:
            print(str(count) + " x " + str(k) + "c")
            
            
   
