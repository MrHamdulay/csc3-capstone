#Grant Meeser
#MSRGRA002
#24/04/2014

print('Enter strings (end with DONE):')
x=''
maxlen=0
lis = []

while x!='DONE':
	x=input('')
	if x == 'DONE':break
	lis.append(x)
	if len(x)>maxlen: maxlen=len(x)

print('\nRight-aligned list:')

for item in lis:
	print((' '*(maxlen-len(item)))+item)

