#MSRGRA002
#Grant Meeser
#03/04/2014

def decimal_to_ndom(d):
	s=''
	while (d>0):	
		s=str(d%6)+s
		d=(d//6)

	return s

def ndom_to_decimal(d):
	s=str(d)
	result=0
	for i in s[0:len(s)-1:1]:
		result=(result+int(i))*6
	result=result+int(s[-1])
	return result

def ndom_add (a, b):
	return decimal_to_ndom(ndom_to_decimal(a)+ndom_to_decimal(b))

def ndom_multiply (a, b):
	return decimal_to_ndom(ndom_to_decimal(a)*ndom_to_decimal(b))
