def prime_s(x):
	if x>1:
		for a in range(2,x):
			if (x%a == 0): 
				return False 
				break
		print(x)
	
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start,end):
	if str(i) == str(i)[::-1] and i>start: 	
		prime_s(i)
	
	
		