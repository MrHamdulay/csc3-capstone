# Student Number: PRTNIC017
# Date: 3/16/14

message = input('Enter the message:\n')
rep_count = eval(input('Enter the message repeat count:\n'))
thickness = eval(input('Enter the frame thickness:\n'))

for nona in range(0, thickness, 1):
    print('|' * nona, '+', '-' * (len(message) - 2 * nona + 2 * thickness), '+', '|' * nona, sep='')

for non in range(rep_count):
    print('|' * thickness, message, '|' * thickness)

for nona in range(thickness - 1, -1, -1):
    print('|' * nona, '+', '-' * (len(message) - 2 * nona + 2 * thickness), '+', '|' * nona, sep='')
