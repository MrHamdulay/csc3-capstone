#Emile McLennan
#Q1
#14/4/14
cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
oneD = False
quart= False
tenT= False
fiveT= False
penny= False
totaldeposit=0
while totaldeposit < cost:
    deposit= eval(input("Deposit a coin or note (in cents):\n"))
    totaldeposit+=deposit
    if totaldeposit ==cost:
        print()
        break
    if (cost-totaldeposit)<0:
        change=totaldeposit-cost
        oneDollar=change//1
        num=change-oneDollar
        quarter=round(num/0.25)
        num=num-(0.25*quarter)
        ten=round(num/0.10)
        num=num-(0.10*ten)
        five=round(num/0.05)
        num=num-(0.05*five)
        num= int(num//0.01)
        print("Your change is:")
        if change>=100:
            print(change//100,"x $1")
        change= change%100
        if change>= 25:
            print(change//25,"x 25c")
        change=change%25
        if change>=10:
            print(change//10,"x 10c")
        change= change%10
        if change>=5:
            print("1 x 5c")
        change= change%5
        if change>=1:
            print(change,"x 1c")
            
        
            
        
        