def vending():
    price = eval(input("Enter the cost (in cents):\n")) #Ask for the money
    
    money = 0
    while money < price: # Will run a loop till there is no change left
        
        money += eval(input("Deposit a coin or note (in cents):\n"))
    
    change = money - price
    if change != 0:
        dollars = change // 100
    
        change -= dollars * 100   
        twentyfives = change // 25
    
        change -= twentyfives * 25
        tens = change // 10
    
        change -= tens * 10
        fives = change // 5
    
        change -= fives * 5
        ones = change // 1
        
        
        print("Your change is:")
        if dollars > 0:
                print(dollars, "x", "$1")
        elif twentyfives > 0:
                print(twentyfives, "x", "25c")
        elif tens > 0:
                print(tens, "x", "10c")
        elif fives > 0:
                print(fives, "x", "5c")
        elif ones > 0:
                print(ones, "x", "1c")
   
vending()    