#Question2.py
#A program calculating the cost of a good and producing the correct change for money paid
#Author: Michelle Njoroge
#Assignment 5
#15 April 2014

def main():
    cost=eval(input("Enter the cost (in cents):\n"))
    if cost>0:
        payment=eval(input("Deposit a coin or note (in cents):\n"))
        x=0 #initialises the value of x

#continue to ask the user for input until the payment is greater than the cost
        while payment<cost:
            x=eval(input("Deposit a coin or note (in cents):\n"))
            payment=payment+x #increases the value of payment
        
        change=payment-cost
        var=0 #initialises the value of var
        if change>0:
            print("Your change is:")    
            
        if change>=100:
            var=change//100
            change=change%(var*100)
            print(var,"x","$1")
    
        if change>=25:
            var=change//25
            change=change%(var*25)
            print(var,"x","25c")
    
        if change>=10:
            var=change//10
            change=change%(var*10)
            print(var,"x","10c")
            
        if change>=5:
            var=change//5
            change=change%(var*5)
            print(var,"x","5c")
   
        if change>=1:
            var=change//1
            change=change%(var*1)
            print(var,"x","1c")
            
    else:
        print() #Print a new line
main()

