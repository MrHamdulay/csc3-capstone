mark = input('Enter a space-separated list of marks:\n')

arrM = []
arrM = mark.split(" ")

fail = 0
third = 0
lsec = 0
usec = 0
first = 0

for k in arrM:
    if eval(k) >= 75:
        first += 1
    elif (eval(k) >= 70) and (eval(k) < 75):
        usec += 1
    elif (eval(k) >= 60) and (eval(k) < 70):
        lsec += 1 
    elif (eval(k) >= 50) and (eval(k) < 60):
        third += 1    
    else:
        fail += 1

print('1 |', 'X' * first, sep='')
print('2+|', 'X' * usec, sep='')
print('2-|', 'X' * lsec, sep='')
print('3 |', 'X' * third, sep='')
print('F |', 'X' * fail, sep='')