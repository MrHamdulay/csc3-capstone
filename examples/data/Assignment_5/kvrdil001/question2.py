#Vending machine
#Dilan Koovarjee
#15 April 2014

cost= eval(input("Enter the cost (in cents):\n"))
deposit= eval(input("Deposit a coin or note (in cents):\n"))
total= deposit

#Loop until requirement is exceeded
while total <cost:
    deposit= eval(input("Deposit a coin or note (in cents):\n"))
    total= total + deposit
if total > cost:
    change= total - cost
    print("Your change is:")
    one_dollar= 0
    quarter= 0
    ten_cents=0
    five_cents=0
    one_cents=0
    while change >0:
        if change/100 >=1:
            one_dollar= change//100
            change= change-(100*one_dollar)
        if change/25 >=1:
            quarter= change//25
            change= change-(25*quarter)
        if change/10 >=1:
            ten_cents= change//10
            change= change-(10*ten_cents)
        if change/5 >= 1:
            five_cents= change//5
            change= change-(5*five_cents)
        if change/1 >=1:
            one_cents= change//1
            change= change-(1*one_cents)
        if one_dollar:
            print(one_dollar,"x $1")
        if quarter:
            print(quarter,"x 25c")
        if ten_cents:
            print(ten_cents,"x 10c")
        if five_cents:
            print(five_cents,"x 5c")
        if one_cents:
            print(one_cents,"x 1c")
    

        

    


