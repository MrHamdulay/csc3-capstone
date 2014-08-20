# Program that prints the triangle
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011

# Prompt user to enter input
height = eval(input("Enter the height of the triangle:\n"))

def main():
	n = height - 1
	count = 1
	for i in range(height):
		shape = "*"
		space = n * " "
		print(space + shape * (2 * count - 1))
		count += 1
		n -= 1

main()