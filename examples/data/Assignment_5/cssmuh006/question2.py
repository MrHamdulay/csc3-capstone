cost=eval(input("Enter the cost (in cents):\n"))
total=0
while(total<cost):
    
    total+=eval(input("Deposit a coin or note (in cents):\n"))
    
change=total-cost
diff=change

oneDol=change//100
change=change%100
tFCents=change//25
change=change%25
tenCents=change//10
change=change%10
fiveCents=change//5
oneCents=change%5

if(diff>0):
    print("Your change is:")
    if(oneDol!=0):
        print(oneDol,"x $1")
    if(tFCents!=0):
        print(tFCents,"x 25c")
    if(tenCents!=0):
        print(tenCents,"x 10c")
    if(fiveCents!=0):
        print(fiveCents,"x 5c")
    if(oneCents!=0):
        print(oneCents,"x 1c")
