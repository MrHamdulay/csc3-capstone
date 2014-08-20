s = eval(input("Enter the starting point N: \n"))
e = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")

if s == 3: i = s + 1
else: i = s

def isprime(x):
	x = abs(int(x))
	if x < 2:
		return "Less 2", False
	elif x == 2:
		return True
	elif x % 2 == 0:
		return False	
	else:
		for n in range(3, int(x**0.5)+2, 2):
			if x % n == 0:
				return n, False
		return True


while i != (e):

    ii = str(i)[::-1]
    if (str(i) == ii) and isprime(i) == True: print(i)
    i = i+1
