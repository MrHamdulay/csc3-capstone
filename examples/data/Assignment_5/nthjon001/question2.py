# vending machine simulator
# Jonathan Nathan
# 12 April 2014

cost=eval(input("Enter the cost (in cents):\n"))
deposit = 0
while deposit < cost:
    deposit+=eval(input("Deposit a coin or note (in cents):\n"))
change = deposit - cost
one_dollar = change//100
twenty_five_cents = (change-(one_dollar*100)) //25
ten_cents = (change-(one_dollar*100)-(twenty_five_cents*25))//10
five_cents = (change-(one_dollar*100)-(twenty_five_cents*25)-(ten_cents*10))//5
cent = (change-(one_dollar*100)-(twenty_five_cents*25)-(ten_cents*10)-(five_cents*5))//1
if change != 0:
    print("Your change is:")
if one_dollar != 0:
    print(one_dollar, 'x $1')
if twenty_five_cents != 0:
    print(twenty_five_cents, 'x 25c')
if ten_cents != 0 :
    print(ten_cents, 'x 10c')
if five_cents != 0:
    print(five_cents, 'x 5c')
if cent != 0:
    print(cent, 'x 1c')