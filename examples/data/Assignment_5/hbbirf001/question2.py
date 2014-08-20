# Vending machine simulation
# Irfan Habib
# 2014/04/16

def main():
    # build 'change wallet'
    list1 = [0,0,0,0,0]
    # get cost
    cost = eval(input('Enter the cost (in cents):\n'))
    # initialise paid
    paid = 0
    # get paid
    if cost != 0:
        while cost > paid:
            paid += eval(input('Deposit a coin or note (in cents):\n'))
        # determine change
        change = paid - cost
        if change != 0: 
            # determine coins for $1
            while change >= 100:
                list1[0] += 1
                change -= 100
            # determine coins for 25c    
            while change >= 25:
                list1[1] += 1
                change -= 25
            # determine coins for 10c
            while change >= 10:
                list1[2] += 1
                change -= 10
            # determine coins for 5c
            while change >= 5:
                list1[3] += 1
                change -= 5
            # determine coins for 1c    
            while change >= 1:
                list1[4] += 1
                change -= 1
            # output
            print('Your change is:')
            if list1[0] > 0:
                print(str(list1[0]) + ' x ' + '$1')
            if list1[1] > 0:
                print(str(list1[1]) + ' x ' + '25c')
            if list1[2] > 0:
                print(str(list1[2]) + ' x ' + '10c') 
            if list1[3] > 0:
                print(str(list1[3]) + ' x ' + '5c')
            if list1[4] > 0:
                print(str(list1[4]) + ' x ' + '1c')      
    
main()