'''This program simulates a vending machine and calculate change based on the amount paid in $ and the change only given with the following:1c, 5c, 10c, 25c, $1
Kouame KOUASSI
12 april 2014'''

def vending_machine():
    deposit = 0 
    #get the cost of the item(s) purchased
    cost = eval(input('Enter the cost (in cents):\n'))
    #ask for money to pay when cost is greater than 0 and ask for more deposit when not enough
    while deposit < cost:
        deposit += eval(input('Deposit a coin or note (in cents):\n'))
    change = deposit - cost
    #Give change when due
    if change > 0:
        print('Your change is:')
        
        for i in (100, 25, 10, 5, 1):
            #check decreasingly if one of the possible coin is part of the change
            if change >= i:
                #specify for change more than or equal to $1 as in dollar               
                if i == 100:
                    print(change//i, ' x ', '$1',sep = '')
                else:
                    print(change//i, ' x ', i,'c',sep = '')
                change -= (change//i)*i
                #check until chanege is 0 then break loop
                if change == 0:
                    break
            else:
                continue

def main():
    vending_machine()
    
if __name__ == "__main__":
    main()
    