# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

n = input("Enter n:\n")
k = input("Enter k:\n")

def get_integer(x):
	x = eval (x)   

def calc_factorial(y):
	yfactorial = 1
	for i in range (1, y+1):
		yfactorial *= i
	return yfactorial
