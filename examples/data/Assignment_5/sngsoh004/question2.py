#SNGSOH004
#Assignment 5
#Question2

cost = eval(input("Enter the cost (in cents):\n"))

if (cost!=0): #As long as the cost is not 0
    deposit=eval(input("Deposit a coin or note (in cents):\n"))
    remainder = cost-deposit
    
    while (remainder>0): #While there is still money outstanding:
        deposit+=eval(input("Deposit a coin or note (in cents):\n"))
        remainder = cost-deposit
        
    string = str(abs(remainder)) #Storing the remainder in a string for future string handling
    
    if(eval(string)>0): #If the value in the string is greater than 0 (person has overpaid)
        onedollar="0"
        if(len(string)>2):
            onedollar = string[:-2] #The amount of $1 bills to be paid back
        cents = eval(string[-2:])
        twentyfive = cents//25 #The number of twenty five cents coins to be paid back
        cents = cents%25 #Reducing the change amount
        ten = cents//10 #The number of ten cents coins to be paid back
        cents = cents%10 #Reducing the change amount
        five = cents//5 #The number of five cents coins to be paid back
        cents = cents%5 #Reducing the change amount
        one = cents//1 #The number of one cent coins to be paid back
        
        print("Your change is:")
        if(eval(onedollar)>0):
            print(onedollar+" x $1")
        if(twentyfive>0):
            print(twentyfive,"x 25c")
        if(ten>0):
            print(ten,"x 10c")
        if(five>0):
            print(five,"x 5c")
        if(one>0):
            print(one,"x 1c")