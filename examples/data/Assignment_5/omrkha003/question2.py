# program to simulate a vending machine and calculate change based on the amount paid
# by: khadeejah omar
# 13 april 2014

cost = eval(input("Enter the cost (in cents): \n"))

payment = 0

# loop until the user's payment is more than or equivalent to the cost
while payment < cost : 
    deposit = eval(input("Deposit a coin or note (in cents): \n"))
    payment += deposit

change = payment - cost

for i in range(1) :
    
    # if the payment exceeds the cost
    if change != 0 : 
        if change >= 100 :
            DollarsChange = change//100
            change = change - (DollarsChange * 100)
            DollarsStr = str(DollarsChange) + " x $1 \n"
        else: 
            DollarsStr = ""
        
        if 25 <= change < 100 :
            T_FiveCentsChange = change//25
            change = change - (T_FiveCentsChange * 25)
            T_FiveStr = str(T_FiveCentsChange) + " x 25c \n"
        else :
            T_FiveStr = ""
        
        if 10 <= change < 25 :
            TenCentsChange = change//10
            change = change - (TenCentsChange * 10)
            TenStr = str(TenCentsChange) + " x 10c \n"
        else : 
            TenStr = ""
        
        if 5 <= change < 10 :
            FiveCentsChange = change//5
            change = change - (FiveCentsChange * 5)
            FiveStr = str(FiveCentsChange) + " x 5c \n"
        else:  
            FiveStr = ""
        
        if 1 <= change < 5 :
            OneCentChange = change
            OneStr = str(OneCentChange) + " x 1c \n"
        else: 
            OneStr = ""
        
        print("Your change is: \n" + DollarsStr + T_FiveStr + TenStr + FiveStr + OneStr)
    
    # if the payment is equivalent to the cost    
    else: 
        break    