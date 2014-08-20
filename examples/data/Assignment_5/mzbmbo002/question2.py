#Mbongeni Mazibuko
#MZBMBO002
#Assignment 5

def coins(change):
    result=''
    dollar=100
    quarter=25
    dime=10
    nickel=5
    penny=1
    numdol, numquart, numdime, numnick, numpen= 0,0,0,0,0
    
    while (change-dollar*numdol)>=0:
        numdol+=1
    temp=(change-(numdol-1)*dollar)
    if numdol-1!=0:
        result+= str(numdol-1)+ ' x '+ '$1\n'
    
    while (temp-quarter*numquart)>=0:
        numquart+=1
    temp=(temp-(numquart-1)*quarter)
    if numquart-1!=0:
        result+= str(numquart-1)+ ' x '+ '25c\n'
    
    while (temp-dime*numdime)>=0:
        numdime+=1
    temp=(temp-(numdime-1)*dime)
    if numdime-1!=0:
        result+= str(numdime-1)+ ' x '+ '10c\n'
    
    while (temp-nickel*numnick)>=0:
        numnick+=1
    temp=(temp-(numnick-1)*nickel)
    if numnick-1!=0:
        result+= str(numnick-1)+ ' x '+ '5c\n'
    
    while (temp-penny*numpen)>=0:
        numpen+=1
    temp=(temp-(numpen-1)*penny)
    if numpen-1!=0:
        result+= str(numpen-1)+ ' x '+ '1c'
    return result

cost = eval(input('Enter the cost (in cents):\n'))
deposit=0

while deposit<cost:
    deposit+=eval(input('Deposit a coin or note (in cents):\n'))
    if deposit>=cost:
        change= deposit-cost
        if change!=0:
            print('Your change is:', coins(change), sep='\n')