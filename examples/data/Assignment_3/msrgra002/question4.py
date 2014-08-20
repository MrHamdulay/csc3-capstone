#Grant Meeser
#MSRGRA002
#25/03/2014

def palen(s):
	s=str(s)
	if s[::-1]==s:
		return True
	else:
		return False

def prime(x):
	x=int(x)
	if x>1:
		result=True
	else:
		result=False
	for i in range(2,x):
		if x%i==0:
			result=False
	return result

start = int(input('Enter the starting point N:\n'))+1
end = int(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
for i in range(start,end):
	if palen(i):
		if prime(i):
			print(i)
