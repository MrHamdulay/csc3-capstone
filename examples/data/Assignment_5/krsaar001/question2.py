#Aaron Krishna 
#15 April 2014
#A program to simulate a vending machine and calculate change based on the amount paid

paid = 0 #creates a variable to store the total amount paid

def paid_calc(): #calculates the total amount paid
    global paid #enables function to use a variable outside the function
    deposit = int(input("Deposit a coin or note (in cents):\n")) #requests user to enter the amount they want to deposit
    paid += deposit
    
def change_calc(): #calculates the change
    change = paid - cost
    
    if change//100: #calculates the number of dollars
        print(change//100, "x $1")
        change %= 100
        
    if change//25: #calculates the number of 25c
        print(change//25, "x 25c")
        change %= 25
        
    if change//10: #calculates the number of 10c
        print(change//10, "x 10c")
        change %= 10
        
    if change//5: #calculates the number of 5c
        print(change//5, "x 5c")
        change %= 5
    
    if change//1: #calculates the number of 1c
        print(change, "x 1c")
   
   
cost = eval(input("Enter the cost (in cents):\n"))

while cost > paid:
    paid_calc()
    
if (paid - cost) != 0:
    print("Your change is:")
    change_calc()