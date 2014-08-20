#Grant Meeser
#MSRGRA002
#02/05/2014

print('Enter strings (end with DONE):')
x=''
maxlen=0
lis = []
printed=[]

while x!='DONE':
	x=input('')
	if x == 'DONE':break
	lis.append(x)
	if len(x)>maxlen: maxlen=len(x)

print('\nUnique list:')

for item in lis:
	if item not in printed:
		print(item)
		printed.append(item)

