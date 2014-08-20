def isprime(n):
	if n == 2:
		return True
	if not n % 2 or n == 1:
		return False
	for i in range(2, n):
		if not n % i:
			return False
	return True

start = int(input('Enter the starting point N:\n'))
end = int(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
for i in range(start + 1, end):
	if not isprime(i):
		continue
	if str(i) == str(i)[::-1]:
		print(i)
		
	
