# vending machine
# anna borysova
# 2014-04-15


cost = int(input("Enter the cost (in cents):\n"))

# ask for moaar monies
pay = 0
while cost > pay:
    pay += int(input("Deposit a coin or note (in cents):\n"))
    
diff = pay - cost

change = ""

for i in [100, 25, 10, 5, 1]:
    num_coin = 0
    # find how many of each denom go into diff
    while diff >= i:
        diff -= i
        num_coin += 1
    # if 0 coins of denomination in change, add nothing
    if num_coin == 0:
        continue
    # special case $
    if i == 100:
        change += str(num_coin)+" x $1\n"
    # add coin number to string output 
    else:
        change += str(num_coin)+" x "+str(i)+"c\n"
if change != "":
     print("Your change is:",change, sep="\n")