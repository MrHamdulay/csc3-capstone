#Nikhil Jiten Naik
#Comsci 1015F
#Assignment 5

def mainMethod():
    
    totalDeposit = 0
    
    changeDollar =0
    changeQuarter =0
    changeTenC  = 0
    changeFiveC = 0
    changeOneC =0
    
    price = eval(input("Enter the cost (in cents): \n"))
    
    while totalDeposit<price:
        deposit = eval(input("Deposit a coin or note (in cents): \n"))
        totalDeposit = totalDeposit + deposit
    
    change = totalDeposit - price
    
   
    while change >= 100:
        change = change -100
        changeDollar +=1
        
    while change >= 25:
        change = change -25
        changeQuarter +=1
    
    while change >= 10:
        change = change -10
        changeTenC +=1
    
    while change >= 5:
        change = change -5
        changeFiveC +=1
    
    while change >= 1:
        change = change -1
        changeOneC +=1

    if changeDollar>0 or changeQuarter>0 or changeTenC >0 or changeFiveC>0 or changeOneC>0:
        
        print("Your change is: ")
        if changeDollar>0:
            print(changeDollar,"x $1")
        if changeQuarter>0:
            print(changeQuarter,"x 25c")
        if changeTenC>0:
            print(changeTenC,"x 10c")
        if changeFiveC>0:
            print(changeFiveC,"x 5c")
        if changeOneC>0:
            print(changeOneC,"x 1c")
    
mainMethod()
    
    
    
    
    
    
        
        