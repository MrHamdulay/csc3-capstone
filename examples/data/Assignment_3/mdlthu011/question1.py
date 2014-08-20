# A a program to draw a rectangle of a given 
# height and width using the ‘*’ character.
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011

def main():
	# Prompt the user for input
	height = eval(input("Enter the height of the rectangle:\n"))
	width = eval(input("Enter the width of the rectangle:\n"))
	for i in range(height):
		shape = "*" * width
		print(shape)

# Call function main()
main()
