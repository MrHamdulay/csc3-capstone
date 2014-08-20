"""a program to simulate a vending machine and calculate change.
Yondela Nkwali
14 April 2014"""

#Get the cost
cost=eval(input("Enter the cost (in cents):\n"))
#ask for money deposited
if cost>0:
    deposit1=eval(input("Deposit a coin or note (in cents):\n"))
    while deposit1<cost:
        deposit2=eval(input("Deposit a coin or note (in cents):\n"))
        deposit1+=deposit2

    change=deposit1-cost #use algebra to calculate the change
    #give change back in coins(1c,5c,10c,25c,$1)
    if change >0:
        print("Your change is:")
    if change>= 100:
        newchange1= (change)//100
        print(newchange1," x $1",sep="") #need to inc this newchange
        change=change-(newchange1*100)
    if change>=25:
        newchange2=change//25
        print(newchange2," x 25c",sep="")
        change=change-(newchange2*25)
    if change>=10:
        newchange3=change//10
        print(newchange3," x 10c",sep="")
        change=change-(newchange3*10)
    if change>=5:
        newchange4=change//5
        print(newchange4," x 5c",sep="")
        change=change-(newchange4*5)
    if change>=1:
        newchange5=change//1
        print(newchange5," x 1c",sep="")
                
        
    
