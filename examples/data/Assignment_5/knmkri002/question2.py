"""Vending Machine to calculate change based on the amount paid
Kristin Kinmont
13 April 2014 """

cost = eval(input("Enter the cost (in cents):\n"))
if cost != 0: # only ask for change if cost is > 0
    paid = eval(input("Deposit a coin or note (in cents):\n"))
    while paid  < cost: # ask for more money if paid amount is less than amount due
        paid += eval(input("Deposit a coin or note (in cents):\n"))
    change = paid - cost
    if change == 0:
        print()
    else:
        print("Your change is:")
        dollars = change//100 # calculate number dollars
        remaining = change%100
        twenty5 = remaining//25 # calculate number 25c
        remaining = remaining%25
        tens = remaining//10 #calculate number 10c
        remaining = remaining%10
        fives = remaining//5 #calculate number 5c
        remaining = remaining%5
        ones = remaining # remaining change is the 1c's
        # only print amounts if they exist, ie >0
        if dollars != 0:
            print(dollars,"x","$1")
        if twenty5 != 0:
            print(twenty5,"x","25c")
        if tens != 0:
            print(tens,"x","10c")
        if fives != 0:
            print(fives,"x","5c")
        if ones != 0:
            print(ones,"x","1c")
        
        
