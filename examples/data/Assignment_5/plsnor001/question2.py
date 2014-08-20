#-------------------------------------------------------------------------------
# Name:        question2
# Purpose:   a program to simulate a vending machine and calculate change based on the amount paid
# Author:      Pilusa
# Created:     14-04-2014
# Copyright:   (c) Pilusa 2014
#-------------------------------------------------------------------------------

def main():
    cost=eval(input('Enter the cost (in cents):\n'))
    coin=0
    while cost!=0:
        deposit=eval(input('Deposit a coin or note (in cents):\n'))
        coin+=deposit #adds deposit to the coins in machine
        if coin==cost:break #breaks loop if coins in machine is the same as cost

        elif coin<cost:
            deposit #asks for more coins if 'coin' is not enough

        elif coin>cost:
            change=coin-cost
            print('Your change is:')

            while True:
                if change>=100:
                    h=change//100
                    print(h,'x $1')
                    change=change%100
                    continue

                if 25<=change<100:
                    t=change//25
                    print(t,'x 25c')
                    change=change%25
                    continue

                if 10<=change:
                    ten=change//10
                    print(ten,'x 10c')
                    change=change%10
                    continue

                if 5<=change:
                    f=change//5
                    print(f,'x 5c')
                    change=change%5
                    continue
                if 0<change:
                    print(change,'x 1c')
                    break

                elif change<=0:
                    break
            break


if __name__ == '__main__':
    main()
