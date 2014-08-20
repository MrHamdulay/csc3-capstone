# Question 2 - Assignment 5
# Oliver Harrison
# 13 April 2014

def main():
    paid=0
    hundred=""
    twentyfive=""
    ten=""
    five=""
    one=""
    
    cost=eval(input("Enter the cost (in cents): \n"))
    while paid<cost:
        deposit=eval(input("Deposit a coin or note (in cents): \n"))
        paid+=deposit
        
    
    change=paid-cost
    if paid>cost:
        print("Your change is:")
        while change!=0:
            if change/100>+1:
                hundred=change//100
                change=change-(100*hundred)
            if change/25>=1:
                twentyfive=change//25
                change=change - (25*twentyfive)
            if change/10>=1:
                ten=change//10
                change=change - (10*ten)
            if change/5>=1:
                five=change//5
                change=change - (5*five)
            if change/1>=1:
                one=change//1
                change = change - (one*1)
            else:
                break
            
        if hundred!="":
            print (hundred, "x $1")
        if twentyfive!="":
            print(twentyfive, "x 25c")
        if ten!="":
            print(ten, "x 10c")
        if five!="":
            print(five, "x 5c")
        if one!="":
            print(one, "x 1c") 
        


main()