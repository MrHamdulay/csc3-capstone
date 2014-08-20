"""Question2 Assignment5
Skhulile Thenjwayo
16 April 2014"""


#enter cost
cost = eval(input("Enter the cost (in cents):\n"))
deposited =0
quart=0
while deposited < cost:
    deposited += eval(input("Deposit a coin or note (in cents):\n"))
change = deposited - cost 
if change != 0:
    print("Your change is:")
if change >=100:
    dollar = change -change%100
    print(dollar//100,"x $1")
    change-=dollar
if change >= 25:
    quart = change - change%25
    print(quart//25,"x 25c")
    change -=quart
if change >= 10:
    ten = change - change%10
    print(ten//10,"x 10c")    
    change -= ten
if change >= 5:
    five = change - change%5
    print(five//5,"x 5c")    
    change -= five
if change <5 and change >0:
    print(change,"x 1c")