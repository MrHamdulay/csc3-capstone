#Grant Meeser
#MSRGRA002
#15/04/2014



#messages and files
message='no message yet'
file1='The meaning of life is blah blah blah ...'
file2='Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy'
#Print menue
answer=''
while answer.upper()!='X':
	print('Welcome to UCT BBS','MENU','(E)nter a message','(V)iew message','(L)ist files','(D)isplay file','e(X)it',sep='\n',end='\n')	
	answer=input('Enter your selection:\n')

	if answer.upper()=='E': message=input('Enter the message:\n')
	if answer.upper()=='V': print('The message is:',message)
	if answer.upper()=='L': print('List of files:','42.txt, 1015.txt')
	if answer.upper()=='D': 
		chooseFile =input('Enter the filename:\n')
		if chooseFile=='42.txt':
			print(file1)
		elif chooseFile=='1015.txt':
			print(file2)
		else:
			print('File not found')
print('Goodbye!')
	
