#Joy Arendse-Gorvalla
def vending(): #defining a new function
    cost = eval(input("Enter the cost (in cents):\n")) #evaluates user input
    deposit = 0
    while deposit < cost: #loop - stops when deposit is more than cost
        deposit += eval(input("Deposit a coin or note (in cents):\n")) #continue until deposit is more than the cost
    if deposit > cost: #if condition statement
        sum = deposit - cost
        if sum != 0:
            print("Your change is:")
        dollar = sum//100
        if dollar != 0:
            print(dollar,'x $1')
        quarters = (sum - dollar*100)//25
        if quarters != 0:
            print(quarters,'x 25c')
        ten_cents = (sum - dollar*100 - quarters*25)//10
        if ten_cents != 0:
            print(ten_cents,'x 10c')
        five_cents = (sum - dollar*100 - quarters*25 - ten_cents*10)//5
        if five_cents != 0:
            print(five_cents,'x 5c')
        one_cents = (sum - dollar*100 - quarters*25 - ten_cents*10 - five_cents*5)//1
        if one_cents != 0:
            print(one_cents,'x 1c')

vending() #call funtion