"""Program to calculate change
Tinotenda Chemvura CHMTIN004
12 April 2014"""

#_____________________Program Starts Here_________________________________

cost = input("Enter the cost (in cents):\n")
if cost.isdigit():
    cost = eval(cost)
    
    deposit = 0
    if cost > 0:
        
        while deposit < cost:
            cash = eval(input("Deposit a coin or note (in cents):\n"))
            deposit+= cash

        change = deposit - cost
            
        dollars = change//100
        r1 = change%100
        
        c25 = r1//25
        r2 = r1%25
        
        c10 = r2//10
        r3 = r2%10

        c5 = r3//5

        r4 = r3%5
        c1 = r4

        if deposit != cost:
            print("Your change is:")

        if dollars > 0:
    
            print(dollars,"x $1")

        if c25 > 0:
            print(c25,"x 25c")
        
        if c10 > 0:
            print(c10,"x 10c")

        if c5 > 0:
            print(c5,"x 5c")

        if c1 > 0:
            print(c1,"x 1c")
             

#______________________Program Ends Here_________________________#