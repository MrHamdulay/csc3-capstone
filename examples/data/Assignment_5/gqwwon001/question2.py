# A programme to simulate a vending machine and calculate change based on the amount paid
# Wongwa Giqwa
# 14 April 2014

# prompts user for amount

print('Enter the cost (in cents):')
cost=eval(input())
"""print('Deposit a coin or note (in cents):')
deposit=eval(input())"""

# Loop to prompt user for more money if initial deposit is less than cost
deposit=0
while deposit<cost:
    print('Deposit a coin or note (in cents):')
    d=eval(input())
    deposit+=d

# Set initial value of change
change=(deposit)-(cost)

if change >0:

    print("Your change is:")
    # Use if statements to classify and break down change into denominations
    if  change>=100:
        print((change//100),'x $1')
        change = change%100
            
    if change>=25:
        print((change//25),'x 25c')
        change=change%25
                
    if change >=10:
        print((change//10),'x 10c')
        change=change%10
                
    if change >=5:
        print(change//5,'x 5c')
        change=change%5
            
    if change!=0:
        print(change,'x 1c')
    
      
        

