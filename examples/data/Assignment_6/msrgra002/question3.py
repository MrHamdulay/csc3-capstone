#Grant Meeser
#MSRGRA002
#24/04/2014

x=''
dic = []
lis = []

print('''Independent Electoral Commission
--------------------------------
Enter the names of parties (terminated by DONE):''')

while x!='DONE'	:
	x= input()
	if x=='DONE': break
	dic.append(x)
	dic.sort()

print('\nVote counts:')



for party in dic:
	party = party+(' '*(10-len(party)))+' - '+str(dic.count(party))
	if party not in lis:
		lis.append(party)

for item in lis:	
	print(item)
