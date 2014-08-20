#A program to calculate change given a specific cost and payment
#Author: Emiel Zyde
#Date: 17 April 2014

def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    payment = 0
    while payment < cost:
        deposit = eval(input("Deposit a coin or note (in cents):\n"))
        payment = payment + deposit
    change = payment - cost
    if change % 100 == 0:
        dollar_change = change // 100
        if change != 0:
            print("Your change is:")
        if dollar_change != 0:
            print(dollar_change, "x $1")
    elif change % 100 != 0:
        dollar_change = change // 100
        change = change - (dollar_change * 100)
        if change % 25 == 0:
            change25 = change // 25
            print("Your change is:")
            if dollar_change !=0:
                print(dollar_change, "x $1") 
            if change25 != 0:
                print(change25, "x 25c")
        elif change % 25 != 0:
            change25 = change // 25
            change = change - (change25 * 25)
            if change % 10 == 0:
                change10 = change// 10
                print("Your change is:")
                if dollar_change !=0:
                    print(dollar_change, "x $1") 
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
                    if dollar_change != 0:
                        print(dollar_change, "x $1") 
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
                    if dollar_change != 0:
                        print(dollar_change, "x $1") 
                    if change25 != 0:
                        print(change25, "x 25c") 
                    if change10 != 0:
                        print(change10, "x 10c")  
                    if change5 != 0:
                        print(change5, "x 5c")    
                    if change1 != 0:
                        print(change1, "x 1c")
                    
       
main() 