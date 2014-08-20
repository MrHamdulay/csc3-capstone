# A program that calculates the value of PI and
# then computes and displays the area
# of a circle with radius entered by the user.

import math		# importing the math library

def circle():
	# print the welcome message
	print("Approximation of pi: 3.142")
	# prompt the user for radius
	radius = eval(input("Enter the radius:\n"))
	# Compute the value for PI
	d1 = math.sqrt(2)
	d2 = math.sqrt(2 + math.sqrt(2))
	d3 = math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))
	d4 = math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2))))
	d5 = math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))))
	d6 = math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2))))))
	d7 = math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))))))
	d8 = math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2))))))))
	PI = 2 * (2 / d1) * (2 / d2) * (2 / d3) * (2 / d4) * (2 / d5) * (2 / d6) * (2 / d7) * (2 / d8)
	# Compute the area of the circle
	area = pow(radius, 2) * PI
	# Display the results
	print("Area:",round(area, 3))

circle()