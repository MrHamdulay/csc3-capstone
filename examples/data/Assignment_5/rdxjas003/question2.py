cost = eval(input('Enter the cost (in cents):\n'))
x = 0
while x<cost:
    j = eval(input('Deposit a coin or note (in cents):\n'))
    x = x + j
change = x - cost
change1 = change
dollar = 0
quarter = 0
tenth = 0
fiver = 0
cent = 0
while change>0:
    if change>=100:
        change = change - 100
        dollar = dollar + 1
    elif change>=25: 
        change = change - 25
        quarter = quarter + 1
    elif change>=10: 
        change = change - 10
        tenth = tenth + 1 
    elif change>=5: 
        change = change - 5
        fiver = fiver + 1
    elif change>=1: 
        change = change - 1
        cent = cent + 1    

if change1>0:
    print('Your change is:')
if dollar != 0:
    print(str(dollar) + ' x $1')
if quarter != 0:
    print(str(quarter) + ' x 25c')
if tenth != 0:
    print(str(tenth) + ' x 10c')
if fiver != 0:
    print(str(fiver) + ' x 5c')
if cent != 0:
    print(str(cent) + ' x 1c')