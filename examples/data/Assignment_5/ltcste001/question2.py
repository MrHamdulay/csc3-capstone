#vending machine change calculator
#stephanie latchmanan
#16 april 2014


cost=eval(input("Enter the cost (in cents):\n"))     #find cost of item
deposit=0
while deposit<cost:                                  #find value of deposit
    dep=eval(input("Deposit a coin or note (in cents):\n"))
    deposit=deposit+dep
change=deposit-cost                                  #find value of change
ones=int(change//100)
change=change-(ones*100)
twenty5=int(change//25)
change=change-(twenty5*25)
ten=int(change//10)
change=change-(ten*10)
five=int(change//5)
change=change-(five*5)
one=int(change//1)
if deposit-cost != 0:                           #print change in denominations
    print("Your change is:")
if ones!=0:
    print(ones, "x", "$1")
if twenty5!=0:
    print(twenty5, "x", "25c")
if ten!=0:
    print(ten, "x", "10c")
if five!=0:
    print(five, "x", "5c")
if one!=0:
    print(one, "x", "1c")
