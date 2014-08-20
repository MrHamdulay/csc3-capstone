#Grant Meeser
#MSRGRA002
#08/05/2014

def pall(s):
	if round(len(s)/2) != 0:
		if s[0] == s[len(s)-1] and pall(s[1:len(s)-1]):
			return True
		else:
			return False
	else:
		return True

if pall(input('Enter a string:\n')):
	print('Palindrome!')
else:
	print('Not a palindrome!')
