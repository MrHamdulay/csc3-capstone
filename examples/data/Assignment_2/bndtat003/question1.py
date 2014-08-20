# program to determine wether a year is a leap year or not

# Name: Matthew Bandama

# Student number: BNDTAT003

# Date : 13-March-2014






year = eval(input('Enter a year:\n'))

if year%400==0 or (year%4==0 and year%100 != 0):
	
	print(year,'is a leap year.')

else:
	print(year,'is not a leap year.',sep =' ')
