#Rorisang Moseli
#April 2014
#program to calculate change from a vending machine

price=eval(input("Enter the cost (in cents):\n"))
deposit=0
dollar=0
quarter=0
ten=0
five=0
one=0

while deposit<price:
    x = eval(input("Deposit a coin or note (in cents):\n"))
    deposit=deposit+x #deposit is accumulated here to avoid an infinite loop
    
#calculaitng change
change = deposit-price
if change//100>=1:
    dollar = change//100
    change= change%(dollar*100) #new change value
if change//25>=1:
    quarter = change//25
    change = change%(quarter*25)
if change//10>=1:
    ten = change//10
    change = change%(ten*10)
if change//5>=1:
    five = change//5
    change = change%(five*5)
if change//1>=1:
    one  = change//5
    
#display change
if deposit-price!=0:
    print("Your change is:")
if dollar>=1:
    print(dollar,"x $1")
if quarter>=1:
    print(quarter,"x 25c")
if ten>=1:
    print(ten,"x 10c")
if five>=1:
    print(five,"x 5c")
if one>=1:
    print(one,"x 1c")
    
    

    
    
