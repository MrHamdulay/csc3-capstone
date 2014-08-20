#question2
#Micaela Menegaldo

def payment():
    cost=eval(input("Enter the cost (in cents):\n"))
    moneygiven=0
    while cost>0:
        money=eval(input("Deposit a coin or note (in cents):\n"))
        moneygiven+=money
        cost-=money
    change=cost*(-1)
    if change>0:
        print("Your change is:")
        while change>0:
            if change>=100:
                one_dollar=change//100
                change=change%100
                print(one_dollar,"x $1")
            elif change>=25:
                twenty_five=change//25
                change=change%25
                print(twenty_five,"x 25c")
            elif change>=10:
                ten=change//10
                change=change%10
                print(ten,"x 10c")
            elif change>=5:
                five=change//5
                change=change%5
                print(five,"x 5c")
            elif change>0:
                print(change,"x 1c")
                break
    
    
if __name__=='__main__':
    payment()