message = (input('Enter the message:\n'))
rmsg = eval(input('Enter the message repeat count:\n'))
thickness = eval(input('Enter the frame thickness:\n'))
tlen = len(message) + 2 * (1 + thickness)

for i in range(thickness):
    print('|' * i + '+' + '-' * (tlen - 2 * (i + 1)) + '+' + '|' * i)

print(('|' * thickness + ' ' + message + ' ' + '|' * thickness + '\n') * rmsg, end = '')

for i in range(thickness - 1, -1, -1):
    print('|' * i + '+' + '-' * (tlen - 2 * (i + 1)) + '+' + '|' * i)	