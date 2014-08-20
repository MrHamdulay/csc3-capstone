#Tofunmi Olagoke
#OLGMOF001
#Vending Machine
#16 April 2014

cost=eval(input("Enter the cost (in cents):\n"))

deposit=0

#Goes on until customer has paid enough or mor than cost
while deposit<cost:
    money=eval(input("Deposit a coin or note (in cents):\n"))
    deposit=deposit+money

#working out how much change is needed
if deposit>cost:
    print("Your change is:")
    change=deposit-cost
    dollars=change//100 #how many dollars returned
    twentyfives=(change%100)//25 #how many 25 cents returned
    tens=((change%100)%25)//10 #how many 10 cents returned
    fives=(((change%100)%25)%10)//5 #how many 5 cents returned
    ones=((((change%100)%25)%10)%5)//1 #how many 1 cents returned
    
    #printing of change received by customer
    if dollars>0:
        print(dollars, "x $1")
    if twentyfives>0:
        print(twentyfives, "x 25c")
    if tens>0:
        print(tens, "x 10c")
    if fives>0:
        print(fives, "x 5c")
    if ones>0:
        print(ones, "x 1c")

