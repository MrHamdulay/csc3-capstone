#program that simulates a vending machine
#Anthony Jacob
#JCBSHA023

def calc_change(change,coin_value):      #function that calculates the change
    count=0
    while change//coin_value != 0:
        count+=1
        change-=coin_value
    return count

cost=eval(input("Enter the cost (in cents):\n"))      #asking user for the cost
deposit=0
while cost>deposit:                       #while loop to keep asking user for deposit until cost is met
    deposit=deposit+ eval(input("Deposit a coin or note (in cents):\n"))
    
change=deposit-cost

if change!=0:
    print("Your change is:")                  #giving back the change
    for i in [100,25,10,5,1]:
        coin_number=calc_change(change,i)
        change=change-coin_number*i
        
        if i==100 and coin_number>0:
            print(str(coin_number), "x $1")
        elif coin_number != 0:
            print(str(coin_number), "x", str(i) + "c")
                  
    
    
                
