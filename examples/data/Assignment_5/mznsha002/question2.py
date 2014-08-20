# 14 April 2014
# Shaun Muzenda
# Simulating a vending machine so as to calculate change to be given based on amount paid

def main():
    cost = eval(input("Enter the cost (in cents):\n"))      #input the amount of money due
    deposited_count = 0                                     #initial amount of deposited_count
    
    while (deposited_count - cost) < 0:                     
        deposited = eval(input("Deposit a coin or note (in cents):\n"))     #amount of money given so as to pay 
        deposited_count = deposited_count + deposited       #continosly adds amount deposited 
        
        if deposited_count == cost:                         #if the amount deposited equals to the cost due, no change is required to be calculated
            break
        
        elif deposited_count > cost:
            
            change = deposited_count - cost                 #calculates difference between deposited amount and amount due
            print("Your change is:")
            
            rem_1 = int(change/100)                         #divides the deposited amount by 100 and returns the integer value only 
            if rem_1 > 1:
                print(rem_1, "x $1")
            
            change_2 = change - (rem_1 * 100)               #multiplies rem by 100 and subtracts it from the change
            rem_2 = int(change_2/25)
            if rem_2 > 0:
                print(rem_2, "x 25c")
            
            change_3 = change - ((rem_1 * 100) + (rem_2 * 25)) #calculates the new change from the first two rem's
            rem_3 = int(change_3/10)
            if rem_3 > 0:
                print(rem_3, "x 10c")    
            
            change_4 = change - ((rem_1 * 100) + (rem_2 * 25) + (rem_3 * 10)) #calculates the new change from the first three rem's
            rem_4 = int(change_4/5)
            if rem_4 > 0:
                print(rem_4, "x 5c")
            
            change_5 = change - ((rem_1 * 100) + (rem_2 * 25) + (rem_3 * 10) + (rem_4 * 5)) #calculates the new change from the first four rem's
            rem_5 = int(change_5/1)
            if rem_5 > 0:
                print(rem_5, "x 1c")
            

        
main()