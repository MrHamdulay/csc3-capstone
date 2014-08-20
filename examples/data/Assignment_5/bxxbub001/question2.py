#VendingMAchine
#B.B00i
#april 15

def vender():
    pay = 0
    price = eval(input("Enter the cost (in cents):\n")) 
    
    while price > pay:
        pay = pay + (eval(input("Deposit a coin or note (in cents):\n")))
        
    change = pay - price
    
    if(price != pay):
        print("Your change is:")
    
    dollar = change//100
    if dollar > 0:
        print(dollar,"x","$1")
    change = change - (dollar*100)
    
    twentyFive = change//25
    if twentyFive > 0:
        print(twentyFive,"x","25c")
    change = change - (twentyFive * 25)
    
    tens = change//10
    if tens > 0:
        print(tens,"x","10c")
    change = change - (tens * 10) 
    
    fives = change//5
    if fives > 0:
        print(fives,"x","10c")
    change = change - (fives * 10)
    
    ones = change//1
    if ones > 0:
        print(ones,"x","1c")
    change = change - (ones * 1)    
    
vender() 