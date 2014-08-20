#Vending machine program
#Annika Brundyn
#16/04/2014

cost = eval(input("Enter the cost (in cents):\n"))
deposit1= eval(input("Deposit a coin or note (in cents):\n"))
total_deposit=deposit1
    
while total_deposit<cost:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    total_deposit+=deposit

if total_deposit>=cost:
    change=total_deposit-cost
    dollar = change//100
    quarter = (change%100)//25
    tencents = ((change%100)%25)//10
    fivecents = (((change%100)%25)%10)//5
    onecents = ((((change%100)%25)%10)%5)
print("Your change is:")
if dollar>0:
    print(dollar,"x $1")
if quarter>0:
    print(quarter,"x 25c")
if tencents>0:
    print(tencents,"x 10c")
if fivecents>0:
    print(fivecents,"x 5c")
if onecents>0:
    print(onecents,"x 1c")



