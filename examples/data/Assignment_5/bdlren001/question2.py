# Program to simulate vending machine
# Budeli Rendani
# BDLREN001
# 16/04/2014


def main():
    
    x=eval(input("Enter the cost (in cents):\n")) # Obtaining the cost of a product from the user
   
    total=0 # Initializing the total input of money to zero
    while x>total: # Program must continue ask more money to insert while the cost is greater than the inserted money
        y=eval(input("Deposit a coin or note (in cents):\n"))
        total=total+y
        
    b=total-x # Calculating the total change
   
    p=[100,25,10,5,1]
    l=["$1","25c","10c","5c","1c"]
    
    if x==0: # If price of product entered is zero, the program must stop running
        return
  
    if total==x: # If the total money entered is equal to the price of the product, no change must be given
        return

   
    print("Your change is:")
    for i in p:
        n=b//i # Number of coins to be given
        if n>0:
            print(n,"x",l[p.index(i)])
            b=b%i # Making be the new change in order to calculate the number of coins in the next loop iterate
    
    
                
                
main()
        
        
  
    
    
    
    
    
    

    