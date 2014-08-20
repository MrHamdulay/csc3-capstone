#Assignment 5
#Question2
#Shaheen Karodia
#KRDSHA003
#2014-04-14

def main():
    
    cash=0
    cost=eval(input("Enter the cost (in cents):\n")) #Find the cost of the item
    while cash<cost: #continue to interate till enoguh money to cover the cost
        prompt=eval(input("Deposit a coin or note (in cents):\n")) #get user to input money 
        cash=cash+prompt  
    
    change=cash-cost    #work out the total change in cents
    
    dollarcount=0    #initilase dollarcount 
    while change >= 100:   
        change=change-100    #reduce value of change
        dollarcount+=1      #keep track of how many dollars change 
        
    quartercount=0  #initialise quartercount
    while change >= 25: 
        change=change-25
        quartercount+=1  #keep track of quartercount
    
    tencount=0 #initialise tencount
    while change >=10:
        change-=10
        tencount+=1 #keep track of tencount
    
    fivecount=0   #initilise fivecount
    while change>=5:
        change-=5
        fivecount+=1 #keep track of five count
    
    onecount=0 #initialise fivecount
    while change>=1:
        change-=1
        onecount+=1 #keep track of one count
        
    if cost!=cash and cost!=0:  #only print change if the cost isnt zero and user has paid too much
        print("Your change is:")
        if dollarcount>0: #
            print(dollarcount, "x $1")
        if quartercount>0:
            print(quartercount, "x 25c")
        if tencount>0:
            print(tencount, "x 10c")
        if fivecount>0:
            print(fivecount, "x 5c")
        if onecount>0:
            print(onecount, "x 1c")
main()