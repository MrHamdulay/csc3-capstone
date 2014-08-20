#Adam Oosthuizen
#mymath
#17 April 2014


cost = eval(input("Enter the cost (in cents):\n"))
paid        = 0
oneCent     = 0
fiveCent    = 0
tenCent     = 0
twenty5Cent = 0
dollar      = 0
while paid < cost:
    paid += eval(input("Deposit a coin or note (in cents):\n"))

change = paid-cost
if change > 0:

    dollar = (change-(change%100))//100
    change = change%100
    twenty5Cent =(change-(change%25))//25
    change = change%25
    tenCent =(change-(change%10))//10
    change = change%10
    fiveCent =(change-(change%5))//5
    change = change%5
    cent = change
    
    print("Your change is:")
    if dollar >0:
        print(dollar,"x $1")
    if twenty5Cent >0:
        print(twenty5Cent,"x 25c")   
    if tenCent >0:
        print(tenCent,"x 10c") 
    if fiveCent >0:
        print(fiveCent,"x 5c")
    if oneCent > 0:
        print(oneCent,"x 1c")
