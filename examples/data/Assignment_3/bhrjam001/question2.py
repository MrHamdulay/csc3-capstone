def triangle(h):
	base = 2 * h - 1
	for i in range(1, base + 1, 2):
		spaces = (base // 2) - (i // 2)
		print(' ' * spaces + '*' * i)

height = int(input('Enter the height of the triangle:\n'))
triangle(height)

