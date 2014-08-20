#vending mechine
#Kalind Ramnrayan
#15 April 2014

cost=eval(input("Enter the cost (in cents):\n"))
deposit=0
if cost>0:
    deposit=eval(input("Deposit a coin or note (in cents):\n"))

difference=cost-deposit

while difference>0:
    nextdeposit=eval(input("Deposit a coin or note (in cents):\n"))
    deposit=deposit+nextdeposit
    difference=cost-deposit

difference=difference*-1

if difference>0:
    print("Your change is:")

while difference>0:

    if difference>=100:
        number=difference//100
        print(number,"x","$1")
        difference=difference-number*100
    elif difference>=25:
            number=difference//25
            print(number,"x","25c")
            difference=difference-number*25
    elif difference>=10:
            number=difference//10
            print(number,"x","10c")
            difference=difference-number*10
    elif difference>=5:
            number=difference//5
            print(number,"x","5c")
            difference=difference-number*5
    elif difference>=1:
            number=difference//1
            print(number,"x","1c")
            difference=difference-number*1
            
                                
    
    
    
    

