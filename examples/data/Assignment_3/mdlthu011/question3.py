# The program that prints a message within a frame
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011

def main():
	x = input("Enter the message:\n")
	y = eval(input("Enter the message repeat count:\n"))
	z = eval(input("Enter the frame thickness:\n"))


	x = " %s "%x # Add the spaces
	for depth in range(z):
		# depth will be 0 on the first iteration, then 1
		print("|"*depth+"+"+"-"*(len(x)+2*(z-depth-1))+"+"+"|"*depth)
	for repeat in range(y):
		print("|"*z+x+"|"*z)
	for depth in reversed(range(z)):
		# reverse the depth values to start from the inner frame
		print("|"*depth+"+"+"-"*(len(x)+2*(z-depth-1))+"+"+"|"*depth)

main()		# Calling function main