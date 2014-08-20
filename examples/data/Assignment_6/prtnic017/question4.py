# Student Number: PRTNIC017
# Date: 4/22/14

counts = [0] * 5

marks = eval('[' + input('Enter a space-separated list of marks:\n').replace(' ', ',') + ']')

for mark in marks:
    if mark < 50:
        counts[4] += 1
    elif mark < 60:
        counts[3] += 1
    elif mark < 70:
        counts[2] += 1
    elif mark < 75:
        counts[1] += 1
    else:
        counts[0] += 1

print('1 |', 'X' * counts[0], sep='')
print('2+|', 'X' * counts[1], sep='')
print('2-|', 'X' * counts[2], sep='')
print('3 |', 'X' * counts[3], sep='')
print('F |', 'X' * counts[4], sep='')