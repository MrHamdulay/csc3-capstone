# program to help decide wether one should eat dropped food or not

# Mame: Matthew Bandama

# Student Number: BNDTAT003

# Date: 13-Mar-2014


print ('Welcome to the 30 Second Rule Expert')
print ('------------------------------------')
print ('Answer the following questions by ',end='')
print ('selecting from among the options.')

ans1 = input('Did anyone see you? (yes/no)\n')

eat = ('Eat it.')

you = ('Your call.')

no = ('Don\'t eat it.')

dec = ('Decision:')


if ans1 == 'yes':
	ans2 = input('Was it a boss/lover/parent? (yes/no)\n')
	
	if ans2 =='yes':
		
		ans3 = input('Was it expensive? (yes/no)\n')
		
		if ans3 == 'yes':
			ans4 = input('Can you cut off the part that touched the floor? (yes/no)\n')
			
			if ans4 == 'yes':
				print(dec,eat)
			
			else:
				print(dec,you)
		else:
			ans5 = input('Is it chocolate? (yes/no)\n')
			
			if ans5=='yes':
				print(dec,eat)
			else:
				print(dec,no)
	else:
		print(dec,eat)

if ans1=='no':
	ans6 = input('Was it sticky? (yes/no)\n')
	
	if ans6 == 'yes':
		ans7 = input('Is it a raw steak? (yes/no)\n')
		
		if ans7 == 'yes':
			ans8 = input('Are you a puma? (yes/no)\n')
			
			if ans8 =='yes':
				print(dec,eat)
			
			else:
				print(dec,no)
		else:
			ans9 = input('Did the cat lick it? (yes/no)\n')
			
			if ans9 == 'yes':
				ans10 = input('Is your cat healthy? (yes/no)\n')
				
				if ans10 == 'yes':
					print(dec,eat)
				
				else:
					print(dec,you)
					
			else:
				print(dec,eat)
	else:
		ans11 = input('Is it an Emausaurus? (yes/no)\n')
		
		if ans11 == 'yes':
			ans12 = input('Are you a Megalosaurus? (yes/no)\n')
			
			if ans12 == 'yes':
				print(dec,eat)
			
			else:
				print(dec,no)
		else:
			ans13 = input('Did the cat lick it? (yes/no)\n')
			
			if ans13 == 'yes':
				ans14 = input('Is your cat healthy? (yes/no)\n')
				
				if ans14 == 'yes':
					print(dec,eat)
				
				else:
					print(dec,you)
					
			else:
				print(dec,eat)
