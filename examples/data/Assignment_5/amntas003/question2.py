#Tashfia Amin #AMNTAS003 #Due: 17 April 2014

#cost of product is stored as integer
cost=eval(input("Enter the cost (in cents): \n"))

#create variable for payments
pay=0
#will only run while the payment is less than or equal to the cost
while pay < cost:
    payment=eval(input("Deposit a coin or note (in cents): \n"))
    pay+=payment

#create variable for change
change=0 
#calculates amount of change necessary if overpaid, in specified increments
if pay > cost:
    change=pay-cost
    
    dollars= change//100
    twentyfive= (change - dollars*100)//25
    ten= (change - dollars*100 - twentyfive*25)//10
    five= (change - dollars*100 - twentyfive*25 - ten*10)//5
    one= (change - dollars*100 - twentyfive*25 -ten*10 - five*5)//1
    
    print("Your change is:")
    if dollars>0:
        print(dollars, "x $1")
    if twentyfive>0:
        print(twentyfive, "x 25c")
    if ten>0:
        print(ten, "x 10c")
    if five>0:
        print(five, "x 5c")
    if one>0:
        print(one, "x 1c")