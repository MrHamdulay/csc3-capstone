# Programme to calculate change
# Mutali Mashamba
# MSHMUT003
# 15 april 2014

# Get amount from user
amt = int(input("Enter the cost (in cents):\n"))
# Get deposit from user (must be greater or equal to amount)
dep = 0
while dep < amt:
    p = int(input("Deposit a coin or note (in cents):\n"))
    dep = dep + p
    if dep >= amt:
        break
# If deposit is greater than amount,calculate change
chg = dep - amt
d = chg//100
chg = chg - d*100
q = chg//25
chg = chg - q*25
n = chg//10
chg = chg - n*10
di = chg//5
chg = chg - di*5
p = chg//1
chg = chg - p
# Display the change
if dep > amt:
    print("Your change is:")
if d != 0:
    print(d,"x $1")
if q != 0:
    print(q,"x 25c")
if n != 0:
    print(n,"x 10c")
if di != 0:
    print(di,"x 5c")
if p != 0:
    print(p,"x 1c")
# Be happy
    
            