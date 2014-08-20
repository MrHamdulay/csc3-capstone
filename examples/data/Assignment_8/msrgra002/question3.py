#Grant Meeser
#MSRGRA002
#08/05/2014

def encode(s):
	if len(s)>1:
		i=ord(s[0])
		i+=1
		if i>122: i-=26
		if i<96: i-=1
		sub=chr(i)
		return sub+encode(s[1::])
	else:
		i=ord(s[0])
		i+=1
		if i>122: i-=26
		if i<96: i-=1
		sub=chr(i)
		return sub

print('Encrypted message:\n'+encode(input('Enter a message:\n')))


