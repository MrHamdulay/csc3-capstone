#Vending Machine Program 
#Kiran Desraj - DSRKIR001
#12 April 2014


deposit = 0 #set initial deposit to R0 in order to initaiate while loop
cost=eval(input("Enter the cost (in cents):\n"))


while cost>deposit:
    deposit = deposit + eval(input("Deposit a coin or note (in cents):\n"))
change=deposit-cost

if change > 0:
    print("Your change is:")  

if change > 100: # checks to see if remaining change is more than a dollar  
    dollar = change//100
    print(dollar,"x $1")
change = change%100   #makes change equal to remainder

if(change>=25):  # checks to see if remaining change is more than a quarter
    quarter=change//25
    print(quarter,"x 25c")
change=change%25   #makes change equal to remainder

if(change>=10):  # checks to see if remaining change is more than a dime
    dime=change//10
    print(dime,"x 10c")
change=change%10 #makes change equal to remainder 

if(change>=5):   # checks to see if remaining change is more than a nickel 
    nickel=change//5
    print(nickel,"x 5c")
change=change%5 #makes change equal to remainder

if(change>=1):  # checks to see if remaining change is more than a penny 
    penny=change//1
    print(penny,"x 1c") #makes change equal to remainder