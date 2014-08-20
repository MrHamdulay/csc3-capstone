#A program to calculate change based on the amount paid 
#Megan Swartz
#17 April 2014

cost_price = eval(input("Enter the cost (in cents):\n"))

#create a loop that runs until the person has put in enough money to meet the cost
payment = 0
while payment < cost_price:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    payment = payment + deposit 
# this loop quits once the person has put in enough money to meet the cost

change = payment - cost_price

if change % 100 == 0:   #check if the change is perfectly divisible by 100
    
    change_100 = change // 100
    
    if change != 0: 
        print("Your change is:")
        
    if change_100 != 0:
        print(change_100, "x $1")
        
elif change % 100 != 0:
    
    change_100 = change // 100
    change = change - (change_100 * 100)
    
    if change % 25 == 0:
        change25 = change // 25
        print("Your change is:")
        
        if change_100 !=0:
            print(change_100, "x $1")     
        if change25 != 0:
            print(change25, "x 25c")
            
    elif change % 25 != 0:
        change25 = change // 25
        change = change - (change25 * 25)
        
        if change % 10 == 0:
            change10 = change// 10
            print("Your change is:")
            if change_100 !=0:
                print(change_100, "x $1") 
            if change25 != 0:
                print(change25, "x 25c") 
            if change10 != 0:
                print(change10, "x 10c")
                
        elif change % 10 != 0:
            change10 = change // 10
            change = change - (change10 * 10)
            
            if change % 5 == 0:
                change5 = change // 5
                print("Your change is:")
                if change_100 != 0:
                    print(change_100, "x $1") 
                if change25 != 0:
                    print(change25, "x 25c") 
                if change10 != 0:
                    print(change10, "x 10c")  
                if change5 != 0:
                    print(change5, "x 5c")
                    
            elif change % 5 != 0:
                change5 = change // 5
                change = change - (change5 * 5)
                change1 = change // 1
                print("Your change is:")
                if change_100 != 0:
                    print(change_100, "x $1") 
                if change25 != 0:
                    print(change25, "x 25c") 
                if change10 != 0:
                    print(change10, "x 10c")  
                if change5 != 0:
                    print(change5, "x 5c")    
                if change1 != 0:
                    print(change1, "x 1c")
                    
       
