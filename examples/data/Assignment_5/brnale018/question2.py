#Program simulating a vending machine
#By Alexander Brunette
#15/04/2014

def main():
    cost=eval(input("Enter the cost (in cents):\n"))
    amount_paid=0
    while amount_paid < cost:
        more_money=eval(input("Deposit a coin or note (in cents):\n"))
        amount_paid= more_money + amount_paid
        
    change=amount_paid - cost
    if change %100!=0:
        whole_change=change//100
        change= change - (whole_change*100)
        
        
    elif change%100 == 0:
        whole_change=change//100
        print("Your change is\n")
        print(whole_change , "x $1")
    
        
        
main()        