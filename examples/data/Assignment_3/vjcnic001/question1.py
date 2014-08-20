#Enter the height of the rectangle:
#3
#Enter the width of the rectangle:
#7
#*******
#*******
#*******
height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))
for n in range(height):
	for i in range(width):
		print("*",end="")
	print("")
	