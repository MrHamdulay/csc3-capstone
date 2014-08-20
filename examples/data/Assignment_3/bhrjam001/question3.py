def frameset(msg, count, size):
	width = len(msg) + 2
	for i in range(0, size):
		bars = width - (2 * i + 2) + size * 2
		print('|' * (i) + '+' + '-' * bars + '+' + '|' * (i))
	for i in range(0, count):
		print('|' * size + ' ' +  msg + ' ' + '|' * size)
	for i in range(size - 1, -1, -1):
		bars = width - (2 * i + 2) + size * 2
		print('|' * (i) + '+' + '-' * bars + '+' + '|' * (i))

message = input('Enter the message:\n')
times = int(input('Enter the message repeat count:\n'))
thickness = int(input('Enter the frame thickness:\n'))
frameset(message, times, thickness)
