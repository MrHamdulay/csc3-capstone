import math
N = eval(input('Enter the starting point N:\n'))
M = eval(input('Enter the ending point M:\n'))

print('The palindromic primes are:')

for k in range(N + 1, M): #Bigger Loop
    if len(str(k)) >= 1: #Only number > 9
        
        Prime = True
        
        Root = int(math.sqrt(k)) + 1
        for j in range(2, Root):
            if k%j == 0:
                Prime = False
                continue
        
        Number = str(k)
        Palin = Number[::-1]
        
        if (Palin == Number) and (Prime == True):
            print(Number)