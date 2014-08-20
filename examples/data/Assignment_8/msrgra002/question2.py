#Grant Meeser
#MSRGRA002
#08/05/2014

counter = 0

def pairs(s):
	global counter
	if len(s)>1:
		if s[0] == s[1]:
			counter+=1
			pairs(s[2::])
		else:
			pairs(s[1::])

pairs(input('Enter a message:\n'))
print('Number of pairs: '+str(counter))
