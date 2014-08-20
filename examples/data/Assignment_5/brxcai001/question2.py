#Program to simulate vending machine and calculate hange based on amount paid.
#BRXCAI001
#16 April 2014


#enter cost and then amount paid.
cost = eval(input("Enter the cost (in cents):\n"))
paid = eval(input("Deposit a coin or note (in cents):\n"))
totalpayment=''

#if user has not paid enough run the deposit option again and then sum the total payment to however much the user has deposited.
if cost>paid:
    newpayment = eval(input("Deposit a coin or note (in cents):\n"))
    totalpayment= paid+newpayment
elif cost<paid:
    totalpayment=paid
    
#calculate the amount of change by subtracting the total payment from the cost.
#calculate different amount of change by dividing the total change by specific money amounts and then change the total change based on how much change has already been given.
change = totalpayment-cost
if change !=0:
    print("Your change is:")
    change1D= change//100
    if change1D > 0:
        print(change1D, "x $1")
    change = change - change1D*100
    change25c= change//25
    if change25c > 0:
        print(change25c, "x 25c")
    change = change - change25c*25
    change10c= change//10
    if change10c > 0:
        print(change10c, "x 10c")
    change = change - change10c*10
    change5c= change//5
    if change5c > 0:
        print(change5c, "x 5c")
    change = change- change5c*5
    change1c= change//1
    if change1c > 0:
        print(change, "x 1c")
        
    
    

    

    


                  
                  