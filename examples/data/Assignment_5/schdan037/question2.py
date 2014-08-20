"""Daniel Schwartz
question 2
april 2014"""


def change(cost, cash):
    """Calculates the change with the cost and cash inputs
    prints change as it calculates"""

    cash -= cost        # pays for the item

    # initial change check
    if cash != 0:
        print("Your change is:")
        if cash >= 100:
            dollar = cash//100
            cash -= dollar * 100
            print(str(dollar) + " x $1")

        # 25 cent check
        if cash >= 25:
            c_25 = cash // 25
            cash -= c_25 * 25
            print(str(c_25) + " x 25c")

        # 10 cent check
        if cash >= 10:
            c_10 = cash // 10
            cash -= c_10 * 10
            print(str(c_10) + " x 10c")

        # 5 cent check
        if cash >= 5:
            c_5 = cash// 5
            cash -= c_5 * 5
            print(str(c_5) + " x 5c")

        # 1 cent check
        if cash >= 1:
            c_1 = cash
            cash -= c_1
            print(str(c_1) + " x 1c")



def main():
    """main"""
    cost = eval(input("Enter the cost (in cents):\n"))
    if cost != 0:
        cash = eval(input("Deposit a coin or note (in cents):\n"))

        # Keeps asking till enough cash deposited
        while cash < cost:
            cash += eval(input("Deposit a coin or note (in cents):\n"))
        
        change(cost, cash)


# runs main on entry
if __name__ == '__main__':
    main()