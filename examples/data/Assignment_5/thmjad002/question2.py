"""Assignment 5, Question 2
Jadon Thomson
14-04-2014"""

def vendor():
    cost = eval(input("Enter the cost (in cents): \n"))
    deposit = 0
    while deposit < cost:
        deposit += eval(input("Deposit a coin or note (in cents): \n"))
    else:
        change = deposit - cost
        _100c = change//100
        _25c = (change%100)//25
        _10c = ((change%100)%25)//10
        _5c = (((change%100)%25)%10)//5
        _1c = (((change%100)%25)%10)%5
        if change != 0:
            print("Your change is:")
            if _100c > 0:
                print(_100c,'x $1')
            if _25c > 0:
                print(_25c, 'x 25c')
            if _10c > 0:
                print(_10c, 'x 10c')
            if _5c > 0:
                print(_5c, 'x 5c')
            if _1c > 0:
                print(_1c, 'x 1c')
        
vendor()

