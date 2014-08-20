# Only works for greedy coin sets
coins = {1:"1c", 5:"5c", 10:"10c", 25:"25c", 100:"$1"}
cost = int(input("Enter the cost (in cents):\n"))
paid = 0
while(paid < cost):
    paid += int(input("Deposit a coin or note (in cents):\n"))
paid -= cost

if (paid > 0):
    print("Your change is:")
    for c in sorted(coins.keys())[::-1]:
        if c > paid:
            continue
        t = int(paid/c)
        paid -= t*c
        print(str(t) + " x " + coins[c])
