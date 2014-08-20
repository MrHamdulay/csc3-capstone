'''Counting the number of paired letters
Sbongakonke Mlangeni
07 April 2014'''

#taking input
x = input('Enter a message:\n')

def pair(x):
    #stopping condition1
    if x == ''  or len(x) == 1:
        return 0
    #counting pairs
    if x[0] == x[1]:
        return 1 + pair(x[2:]) 
    #recursive step
    else:
        return pair(x[1:])

print('Number of pairs:',pair(x))


    