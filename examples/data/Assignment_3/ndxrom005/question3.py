msg = (input('Enter the message:\n'))
rmsge = eval(input('Enter the message repeat count:\n'))
th = eval(input('Enter the frame thickness:\n'))
tlen = len(msg) + 2 * (1 + th)

for i in range(th):
    print('|' * i + '+' + '-' * (tlen - 2 * (i + 1)) + '+' + '|' * i)

print(('|' * th + ' ' + msg + ' ' + '|' * th + '\n') * rmsge, end = '')

for i in range(th - 1, -1, -1):
    print('|' * i + '+' + '-' * (tlen - 2 * (i + 1)) + '+' + '|' * i)