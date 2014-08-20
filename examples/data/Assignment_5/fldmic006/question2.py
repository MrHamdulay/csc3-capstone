#change giver
#Michael Field
#14 April

#get input from user
cost = eval(input("Enter the cost (in cents):\n"))
deposit = 0

#ask user to deposit money until the cost is paid
while deposit < cost:
    deposit += eval(input("Deposit a coin or note (in cents):\n"))

change = deposit - cost

#if the user recieves change
if (change > 0):
    print("Your change is:")
    
    #work out how many dollars to give. subtract from owed change
    dollars = change//100
    change = change - dollars*100
    
    #work out how many quarters to give. subtract from owed change    
    quarters = change//25
    change = change - quarters*25
    
    #work out how many tens to give. subtract from owed change
    tens = change//10
    change = change - tens*10
    
    #work out how many fives to give. subtract from owed change    
    fives = change//5
    change = change - fives*5
    
    #the remainder is the cents    
    ones = change
        
    if (dollars != 0):
        print(dollars, "x $1")
        
    if (quarters != 0):
        print(quarters, "x 25c")
        
    if (tens != 0):
        print(tens, "x 10c")
        
    if (fives != 0):
        print(fives, "x 5c")
        
    if (ones != 0):
        print(ones, "x 1c")    
    
    
    