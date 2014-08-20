# Program for calculating change in a vending machine
# Written by LWazi Shezi
# 14.04.2014

# First input and keep cost in a certain variable
cost=eval(input('Enter the cost (in cents):\n'))

# Before any money is inserted, the deposit is 0
deposit=0

# Start looping and repeat until the cost is less than the deposit
while cost > deposit :
    
# Ask for extra money and add whatever input value the accumulated deposit
    next_deposit=eval(input('Deposit a coin or note (in cents):\n'))
    deposit=deposit+next_deposit
    
# Calculate change in the end
change = deposit - cost

if change !=0:

    print('Your change is:')

    # Find the number of each coins that is required so that enough change is returned and a minimum number of coins is used
    USD1_coins = change //  100
    T5c_coins = (change - USD1_coins*100) // 25
    TENc_coins = (change - USD1_coins*100 - T5c_coins*25) // 10
    FIVEc_coins = (change - USD1_coins*100 - T5c_coins*25 - TENc_coins*10) // 5
    ONEc_coins = (change - USD1_coins*100 - T5c_coins*25 - TENc_coins*10 - FIVEc_coins*5)


    # Output the number of each coins required if they are more than zero.
    if USD1_coins > 0:
        print(USD1_coins,'x','$1')
    
    if T5c_coins > 0:
        print(T5c_coins,'x','25c')
    
    if TENc_coins > 0:
        print(TENc_coins,'x','10c')
    
    if FIVEc_coins > 0:
        print(FIVEc_coins,'x','5c')
    
    if ONEc_coins > 0:
        print(ONEc_coins,'x','1c')