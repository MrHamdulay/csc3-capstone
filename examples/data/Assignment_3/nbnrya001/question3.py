
m = (input('Enter the message:\n'))
r = eval(input('Enter the message repeat count:\n'))
t = eval(input('Enter the frame thickness:\n'))
total = len(m) + 2 * (1 + t)
for i in range(t):
    print('|' * i + '+' + '-' * (total - 2 * (i + 1)) + '+' + '|' * i)
print(('|' * t + ' ' + m + ' ' + '|' * t + '\n') * r, end = '')
for i in range(t - 1, -1, -1):
    print('|' * i + '+' + '-' * (total - 2 * (i + 1)) + '+' + '|' * i)
