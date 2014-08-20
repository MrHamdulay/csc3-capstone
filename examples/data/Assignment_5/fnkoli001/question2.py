# coding=utf-8
cost = eval(input("Enter the cost (in cents):\n"))
if cost != 0:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))

    while deposit < cost:
        deposit += eval(input("Deposit a coin or note (in cents):\n"))

    #Must be greater
    #get change
    change = deposit - cost

    is_change = False
    #Work out the dollars (if there are any)
    #Conv to str for easy manipulation
    str_change = str(change)
    dollars = 0
    if len(str_change) >= 3:
        is_change = True
        dollars = eval(str_change[:-2])
        change -= dollars * 100

    #could be betwenn  0 - 99
    twenty_fives = 0
    while change >= 25:
        is_change = True
        twenty_fives += 1
        change -= 25

    #Could be between 0-24
    tens = 0
    while change >= 10:
        is_change = True
        tens += 1
        change -= 10

    #Could be between 0-9
    fives = 0
    while change >= 5:
        is_change = True
        fives += 1
        change -= 5

    #Could be between 0-4
    ones = change

    #print the change split up
    if is_change or ones > 0:
        print("Your change is:\n", end='')

    if dollars > 0:
        print(str(dollars) + " x $1")
    if twenty_fives > 0:
        print(str(twenty_fives) + " x 25c")
    if tens > 0:
        print(str(tens) + " x 10c")
    if fives > 0:
        print(str(fives) + " x 5c")
    if ones > 0:
        print(str(ones) + " x 1c")