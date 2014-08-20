#Assignment 5, Question 2, calculating the change from a deposit on a cost
#LYLON002
#15 April 2014

deposit = 0
test = True                     #variable to check if running

cost = eval(input("Enter the cost (in cents):\n"))   #ask for cost

if cost == 0:
    test = False                #test change

if test == True:
    while deposit < cost:
        deposit = deposit + eval(input("Deposit a coin or note (in cents):\n")) #get money until more than cost


change = deposit - cost             #calculate change

if change == 0:
    test = False                        #test change

if test == True :                   #test if change necessary
    
    dollars = change // 100
    change = change - dollars*100

    twentyfive = change // 25
    change = change - twentyfive*25

    tens = change // 10
    change = change - tens*10           #calculating the change

    fives = change // 5
    change = change - fives*5

    ones = change // 1
    change = change - ones*1

    print("Your change is:")

    if dollars > 0:
        print(str(dollars) + " x $1")

    if twentyfive > 0:
        print(str(twentyfive) + " x 25c")
    
    if tens > 0:
        print(str(tens) + " x 10c")         #displaying the change from calculation
   
    if fives > 0:
        print(str(fives) + " x 5c")
    
    if ones > 0:
        print(str(ones) + " x 1c")
