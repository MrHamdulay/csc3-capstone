#Question2
#Creating a Vending Machine
#By: Dean de Haast
#14 April 2014

#Initialisng values
total_money = 0
money_received = 0
dollars=0
twenty_fives =0
tens=0
fives=0
ones=0

#Enter price
price=eval(input("Enter the cost (in cents):\n"))

#Receive money
while total_money < price:
    money_received=eval(input("Deposit a coin or note (in cents):\n"))
    total_money += money_received
    
#Calculate Change
change = (total_money-price)
change_original = change

while change > 0:
    if change >99:
        dollars += 1
        change -=100
    elif change > 24:
        twenty_fives +=1
        change-=25
    elif change >9:
        tens +=1
        change-=10
    elif change>4:
        fives +=1
        change -=5
    elif change >0:
        ones+=1
        change -=1

#Printing the Change given
if change_original != 0:
    print("Your change is:")
    if dollars >0:
        print(dollars, "x $1")
    if twenty_fives >0:
        print(twenty_fives, "x 25c")    
    if tens >0:
        print(tens, "x 10c")
    if fives >0:
        print(fives, "x 5c")
    if ones > 0:
        print(ones, "x 1c")