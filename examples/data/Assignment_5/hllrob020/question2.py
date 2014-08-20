#Change program
#Robin Hall
#17/04/2014

cost = eval (input("Enter the cost (in cents):\n")) #price of item

cash = 0 #set initial cash to 0

while cash < cost:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    cash += deposit #keeps prompting user to input money values until cash equals or exceeds cost
    
change = cash - cost #change required
dollar = change//100 #change in dollars
quarter = (change%100)//25 #change in quarters
ten_cent = (change%25)//10 #change in ten cents
five_cent = (change%10)//5 #change in five cents
cent = (change%5) #change in cents

if change > 0: #cannot have negative change
    print("Your change is:")

if change >= 100: #for change amount greater than a dollar
    print(dollar, "x $1")
    if quarter > 0:
        print(quarter, "x 25c")
    if ten_cent > 0:
        print(ten_cent, "x 10c")
    if five_cent > 0:
        print(five_cent, "x 5c")
    if cent > 0:
        print(cent, "x 1c")
    
elif change >= 25: #for change amount greater than a quarter
    print(quarter, "x 25c")
    if ten_cent > 0:
        print(ten_cent, "x 10c")
    if five_cent > 0:
        print(five_cent, "x 5c")
    if cent > 0:
        print(cent, "x 1c")
    
elif change >= 10: #for change amount greater than 10 cents
    print(ten_cent, "x 10c")
    if five_cent > 0:
        print(five_cent, "x 5c")
    if cent > 0:
        print(cent, "x 1c")
    
elif change >= 5: #for change amount greater than 5 cents
    print(five_cent, "x 5c")
    if cent > 0:
        print(cent, "x 1c")
    
elif change >= 5: #for change in cents
    print(cent, "x 1c")