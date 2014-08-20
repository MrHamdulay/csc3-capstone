Mes = input('Enter the message:\n')
Rep = eval(input('Enter the message repeat count:\n'))
Thick = eval(input('Enter the frame thickness:\n'))

Mes = ('|' * Thick) + ' ' + Mes + ' ' + ('|' * Thick)
Length = len(Mes)

iStrike = 0
Count = 1

for k in range(0, Thick):
    print('|' * iStrike, '+', '-' * (Length - (2 * Count)), '+', '|' * iStrike, sep='')
    Count += 1
    iStrike += 1
 
for i in range(0, Rep):
    print(Mes)
    
for m in range(0, Thick):
    Count -= 1
    iStrike -= 1    
    print('|' * iStrike, '+', '-' * (Length - (2 * Count)), '+', '|' * iStrike, sep='')