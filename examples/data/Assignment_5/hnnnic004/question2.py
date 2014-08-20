'''program for giving change
nicole henning
due 17 april'''

cost = eval(input("Enter the cost (in cents):\n"))

if cost !=0:
    payment = eval (input("Deposit a coin or note (in cents):\n"))

    #continue asking until payment covers cost
    while payment < cost !=0:
        next_payment = eval (input("Deposit a coin or note (in cents):\n"))
        payment += next_payment
    
    change = int(payment - cost)
    if change>0:    
        print("Your change is:")
    
    #calculate number of dollars (ie 100c)
    dollars = int(change/100)
    if dollars > 0:
        print(dollars, "x $1")
    
    change -= dollars*100
    
    #calculate number of 25c
    twenty_fives = int(change/25)
    if twenty_fives > 0:
        print(twenty_fives, "x 25c")
    
    change -= twenty_fives*25
    
    #calculate number of 10c
    tens = int(change/10)
    if tens > 0:
        print(tens, "x 10c")
    
    change -= tens*10
    
    #calculate no of 5c
    fives = int(change/5)
    if fives >0:
        print(fives, "x 5c")
    
    change -= fives*5
    
    #calculate numnber of 10c
    ones = int(change/1)
    if ones > 0:
        print(ones, "x 1c")
    
    
