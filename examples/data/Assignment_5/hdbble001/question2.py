cost=eval(input("Enter the cost (in cents):\n"))

total=0

while total < cost:
    dep=eval(input("Deposit a coin or note (in cents):\n"))
    total+=dep
    
def change():
    amount=total-cost
    dollars=amount//100
    quarters=(amount%100)//25
    dimes=((amount%100)%25)//10
    nickels=(((amount%100)%25)%10)//5
    pennies=(((amount%100)%25)%10)%5
    
    if dollars!=0:
        print(dollars, "x $1")
    if quarters!=0:
        print(quarters, "x 25c")
    if dimes!=0:
        print(dimes, "x 10c") 
    if nickels!=0:
        print(nickels, "x 5c") 
    if pennies!=0:
        print(pennies, "x 1c")    

if total-cost!=0:
    print("Your change is:")
    change()