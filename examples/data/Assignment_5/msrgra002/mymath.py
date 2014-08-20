#Grant Meeser
#MSRGRA002
#15/04/2014

def get_integer(s):
	if s=='n':
		n = input ("Enter n:\n")
		while not n.isdigit ():
		   n = input ("Enter n:\n")
		return int(n)
	if s=='k':
		k = input ("Enter k:\n")
		while not k.isdigit ():
		   k = input ("Enter k:\n")
		return int(k)

def calc_factorial(n):
	n=int(n)
	nfactorial = 1
	for i in range(1, n+1):
	   nfactorial *= i
	return nfactorial
	
