# Question 2 - Assignment 5
# Richard van Gysen 

# transaction
     
def transaction():
    
    cost = eval(input("Enter the cost (in cents): \n")) 
    if cost >0:
        paid = eval(input("Deposit a coin or note (in cents): \n"))
        # get more money
        while cost>paid:
            extra = eval(input("Deposit a coin or note (in cents): \n"))
            paid = extra + paid
        # get change    
        if paid>=cost:
                if cost==paid:
                    print()
                if paid>cost:
                    message = ''
                    change = paid - cost
                    dollars = change//100
                    if dollars !=0:
                        message = message + str(dollars)+' x $1\n'
                    change = change - dollars*100    
                    quarters = (change%100)//25
                    if quarters != 0:
                        message = message + str(quarters)+' x 25c\n'
                    change = change - quarters*25    
                    dimes = (change%25)//10
                    if dimes!=0:
                        message = message + str(dimes)+' x 10c\n'
                    change = change - dimes*10    
                    fives = (change%10)//5
                    if fives !=0:
                        message  = message + str(fives)+' x 5c\n'
                    change = change - fives*5    
                    pennies = (change%5)
                    if pennies!=0:
                        message = message + str(pennies)+' x 1c'
                    print("Your change is:\n",message,sep = '')
transaction()