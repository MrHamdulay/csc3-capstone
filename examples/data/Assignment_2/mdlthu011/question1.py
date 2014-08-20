# A program that check if the year is a leap year or not
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011

def leap():
	year = eval(input("Enter a year:\n"))
	# Check if the year is a leap year
	isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
		(year % 400 == 0)
	# Display the result
	if isLeapYear == True:
		print(year, "is a leap year.")
	else:
		print(year, "is not a leap year.")
leap()