cost = eval(input("Enter the cost (in cents):\n"))

DepositTotal = 0

while DepositTotal < cost:
    Deposit = eval(input("Deposit a coin or note (in cents):\n"))
    DepositTotal = DepositTotal + Deposit
    
Change = DepositTotal - cost

z = Change//100

if Change%100 == 0:
    y = 0
else:    
    y = ((Change-(z*100))//25)
   
if (Change-(z*100))%25 == 0:
    x = 0
else:
    x = (((Change-(z*100))%25)//10)
   
if (Change-(y*25))%10 == 0:
    w = 0
else:
    w = ((Change-(x*10))//5)

if (Change-(x*10))%5 == 0:
    v = 0
else:
    v = ((Change-(w*5))//1)

if Change != 0:
    print("Your change is:")
    if z != 0:
        print(z, "x $1")
    if y != 0:
        print(y, "x 25c")
    if x != 0:
        print(x, "x 10c")
    if w != 0:
        print(w, "x 5c")
    if v != 0:
        print(v, "x 1c")