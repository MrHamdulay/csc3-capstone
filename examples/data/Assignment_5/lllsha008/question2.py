
#array of denominations and values in cents they represent
denoms = [[100, '$1'], [25, '25c'], [10, '10c'], [5, '5c'], [1, '1c']]

toget = int(input('Enter the cost (in cents):\n'))
#get input

current = 0

while current < toget:
    current += int(input('Deposit a coin or note (in cents):\n'))
#receive input until greater than ammount owing

change = current - toget

if change != 0:
    #if there is change
    print('Your change is:')

while (change != 0):
    for i in denoms:
        #if the denomination is greater than amount owing
        if change // i[0] == 0:
            continue
        else:
            #give change
            print(change // i[0], 'x', i[1])
            change = change % i[0]
            break
            
