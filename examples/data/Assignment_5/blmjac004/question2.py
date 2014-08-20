cost=eval(input("Enter the cost (in cents):\n"))
i=0
while i<cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    i=i+deposit
change=i-cost
if change!=0:
    print("Your change is:")
if change > 0:
    if change//100!=0:
        print(change//100, "x $1")
    cents=change%100
    if cents//25!=0:
        print(cents//25, "x 25c")
    tenc=cents%25
    if tenc//10!=0:
        print(tenc//10, "x 10c")
    fivec=tenc%10
    if fivec//5!=0:
        print(fivec//5, "x 5c")
    onec=fivec%5
    if onec//1!=0:
        print(onec//1, "x 1c")
        
    