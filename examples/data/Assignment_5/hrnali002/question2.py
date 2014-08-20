# A program to simulate a vending machine
# Alison Hoernle
# HRNALI002
# 12 April 2014

def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    
    if cost != 0:
        first = eval(input("Deposit a coin or note (in cents):\n"))
        payment = first
    
        # pay more if payment is less than the cost
        while payment < cost:
            second = eval(input("Deposit a coin or note (in cents):\n"))
            payment += second
            
        # calculate change
        change = payment - cost
        if change != 0:
            print("Your change is:")
                
        # Use int division and remainder key to determine the number of the different coins given as change
        one_dollar = change // 100
        change1 = change % 100
        twenty_five = change1 // 25
        change2 = change1 % 25
        ten = change2 // 10
        change3 = change2 % 10
        five = change3 // 5
        change4 = change3 % 5
        one = change4 // 1
        
        # If the number of that coin is not 0 then print the number of coins times that coin value
        if one_dollar > 0:
            print(one_dollar, 'x $1')
            
        if twenty_five > 0:
            print(twenty_five, 'x 25c')
            
        if ten > 0:
            print(ten, 'x 10c')
            
        if five > 0:
            print(five, 'x 5c')
            
        if one > 0:
            print(one, 'x 1c')
                    
main()