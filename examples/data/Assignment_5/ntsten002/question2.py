cost = eval(input("Enter the cost (in cents):\n"))

if cost != 0:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    while (deposit < cost and cost != 0):
        deposit+=eval(input("Deposit a coin or note (in cents):\n"))
    else:
        answer = abs(cost-deposit)
        if answer!=0:
            print("Your change is:")        
            while answer != 0:
                if (answer >= 100):
                    print(answer//100, "x $1")
                    answer = answer%100
                elif (answer >= 25):            
                    print(answer//25, "x 25c")
                    answer = answer%25
                elif answer >= 10:            
                    print(answer//10, "x 10c")
                    answer = answer%10
                elif answer >= 5:            
                    print(answer//5, "x 5c")
                    answer = answer%5
                else:
                    print(answer, "x 1c")
                    answer= answer%1

    
        
