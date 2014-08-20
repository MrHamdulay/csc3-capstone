"""vending machine
ringo shima
17/4/14"""

def main():
    
    cost = eval(input("Enter the cost (in cents):\n"))
    value = 0
    while value < cost: #if amount of cash given is still less than cost prompt for more cash
        deposit = eval(input("Deposit a coin or note (in cents):\n"))
        value += deposit #add values together, make total
    
    total = int(value - cost)
    if total != 0:
        dollars = total//100
        remDollars = total %100
        quaters = remDollars//25
        remQuaters = remDollars%25
        tens = remQuaters//10
        remTens = remQuaters%10
        five = remTens//5
        remFive = remTens%5
        one = remFive//1
   
        print("Your change is:")
        if dollars != 0:
            print(dollars, "x $1")
        
        if quaters != 0:
            print(quaters, "x 25c")
        
        if tens != 0:
            print(tens, "x 10c")
        
        if five != 0:
            print(five, "x 5c")
        
        if one != 0:
            print(one, "x 1c")
    
    
main()