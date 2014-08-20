#Assignment 5
#Question 2

cost=eval(input("Enter the cost (in cents):\n"))
deposit=0 #Intialise values to avoid errors
dollar=0
twenty_five=0
ten=0
five=0
one=0

while deposit<cost:
    x= eval(input("Deposit a coin or note (in cents):\n"))
    deposit=deposit+x #Accumulate value for deposit to avoid infinite loop

    
# Calculate change
change= deposit-cost
# Change in $
if change//100>=1:
    dollar= change//100 #How many $1 you get back
    change= change%(dollar*100) #New change value after sorting out $1
if change//25>=1:
    twenty_five = change//25
    change = change%(twenty_five*25)
if change//10>=1:
    ten= change//10
    change= change%(ten*10)
if change//5>=1:
    five= change//5
    change= change%(five*5)
if change//1>= 1:
    one= change//5

#print out change
if deposit-cost!=0: 
    print("Your change is:")
if dollar>=1:
    print(dollar,"x $1")
if twenty_five>=1:
    print(twenty_five,"x 25c")
if ten>=1:
    print(ten,"x 10c")
if five>=1:
    print(five,"x 5c")
if one>=1:
    print(one,"x 1c")
    
    

    
    
              
