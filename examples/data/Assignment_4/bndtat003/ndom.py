# Module that swaps between base 10 and base 6

# Name: Matthew Bandama

# Student Number: BNDTAT003

# Date: 31-March-2014

def ndom_to_decimal(a):
	b = a//100
	c = (a%100)//10
	d = a%10
	
	number = b*36 + c*6 + d
	
	return(number)

def decimal_to_ndom(a):
	hundreth = a//36
	tenth = (a%36)//6
	nth = a%6
	
	if hundreth == 0:
		
		hundreth =''
	
	if hundreth == 0 and tenth == 0:
		tenth = ''
	
	number = str(hundreth)+str(tenth)+str(nth)
	number = eval(number)
	
	return(number)

def ndom_add(a,b):
	
	z = ndom_to_decimal(a)+ndom_to_decimal(b)
	return(decimal_to_ndom(z))

def ndom_multiply(a,b):
	
	z = ndom_to_decimal(a)*ndom_to_decimal(b)
	return(decimal_to_ndom(z))


