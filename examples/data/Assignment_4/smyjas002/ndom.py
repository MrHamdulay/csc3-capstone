def ndom_to_decimal (a):
	total = 0
	strA = str(a)
	digitsA = len(strA)
	x = 0
	for i in range(digitsA-1,-1,-1):
		total += int(strA[x])*(6**i)
		x += 1
	return total
    
def decimal_to_ndom (a):
	digits = ''
	while(True):
		digit = a%6
		a = a//6
		digits += str(digit)
		if a < 6:
			digits += str(a)
			break
	return digits[::-1]
	
def ndom_add (a, b):
	a = ndom_to_decimal (a)
	b = ndom_to_decimal (b)
	add = a + b
	return decimal_to_ndom(add)
	
def ndom_multiply (a, b):
	a = ndom_to_decimal (a)
	b = ndom_to_decimal (b)
	product = a * b
	return decimal_to_ndom(product)
	



'''

    ndom_to_decimal (a), that converts a Ndom number to decimal
    decimal_to_ndom (a), that converts a decimal number to Ndom
    ndom_add (a, b), that adds 2 Ndom numbers
    ndom_multiply (a, b), that multiples 2 Ndom numbers

Sample I/O:

Choose test:
d 12
calling function
called function
20

Sample I/O:

Choose test:
n 20
calling function
called function
12

Sample I/O:

Choose test:
a 123 141
calling function
called function
304

Sample I/O:

Choose test:
m 13 14
calling function
called function
230

'''
