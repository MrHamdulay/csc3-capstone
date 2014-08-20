def vending():
    scost = int(input('Enter the cost (in cents):\n'))
    spayment = 0
    while scost - spayment > 0:
        spayment += int(input('Deposit a coin or note (in cents):\n'))
    schange = spayment - scost
    scoins = [0,0,0,0,0]
    if schange != 0:
        while not schange == 0:
            if schange >= 100:
                scoins[0] += 1
                schange += -100
            elif schange >= 25:
                scoins[1] += 1
                schange += -25
            elif schange >= 10:
                scoins[2] += 1
                schange += -10
            elif schange >= 5:
                scoins[3] += 1
                schange += -5
            else:
                scoins[4] += 1
                schange += -1
        else: print('Your change is:') 
    svalue = ['$1','25c','10c','5c','1c']
    for i in range(5):
        if scoins[i] != 0:
            print(str(scoins[i]),'x',svalue[i])
vending()