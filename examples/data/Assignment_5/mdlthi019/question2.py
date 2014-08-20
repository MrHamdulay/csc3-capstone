"""  program to simulate a vending machine and calculate change based on the amount paid
Thiloshni Moodley(MDLTHI019)
15 April 2014"""


Cost=eval(input("Enter the cost (in cents):\n"))
Total = 0 #initial sum set to 0

while Total < Cost: #prompt user for more coins or notes
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    Total += deposit 
else: #when Total>cost, change needed
    change = Total - Cost
    if change != 0:
        print("Your change is:")
    remainder = change
    
    #change into different coins
    left=change//100
    if left !=0:
        print(str(left)+ ' x $1')
        remainder = change - left*100
        
    if remainder != 0:
        left = remainder//25
        if left !=0:
            print(str(left)+ ' x 25c')
            remainder = remainder - left*25
            
    if remainder != 0:
        left = remainder//10
        if left !=0:
            print(str(left)+ ' x 10c')
            remainder = remainder - left*10 
            
    if remainder != 0:
        left = remainder//5
        if left !=0:
            print(str(left)+ ' x 5c')
            remainder = remainder - left*5 
            
    if remainder != 0:
        left = remainder//1
        if left !=0:
            print(str(left)+ ' x 1c')
            remainder = remainder - left*1    
            
        
    
        
        
         
        
    
           