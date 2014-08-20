#Grant Meeser
#MSRGRA002
#13/02/2014

print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

if( input('Did anyone see you? (yes/no)\n')=='yes'):
	if( input('Was it a boss/lover/parent? (yes/no)\n')=='yes'):
		if( input('Was it expensive? (yes/no)\n')=='yes'):
			if( input('Can you cut off the part that touched the floor? (yes/no)\n')=='yes'):
				print('Decision: Eat it.')
			else: #can you cut it
				print('Decision: Your call.')
		else: #was it expensive
			if( input('Is it chocolate? (yes/no)\n')=='yes'):
				print('Decision: Eat it.')
			else: #was it chocolate
				print("Decision: Don't eat it.")
	else: #was it boss/lover/parent
		print('Decision: Eat it.')
else: #did anyone see no
	if( input('Was it sticky? (yes/no)\n')=='yes'):
		if( input('Is it a raw steak? (yes/no)\n')=='yes'):
			if( input('Are you a puma? (yes/no)\n')=='yes'):
				print('Decision: Eat it.')
			else: #are you a puma
				print("Decision: Don't eat it.")
		else: #is it raw stake
			if( input('Did the cat lick it? (yes/no)\n')=='yes'):
				if( input('Is your cat healthy? (yes/no)\n')=='yes'):
					print('Decision: Eat it.')
				else: #is your cat healthy
					print("Decision: Don't eat it.")
			else: #did the cat lick it
				print('Decision: Eat it.')
	else: #was it sticky
		if( input('Is it an Emausaurus? (yes/no)\n')=='yes'):
			if( input('Are you a Megalosaurus? (yes/no)\n')=='yes'):
				print('Decision: Eat it.')		
			else: #is it raw stake
				print("Decision: Don't eat it.")
		else: #is it an emausaurus
			if( input('Did the cat lick it? (yes/no)\n')=='yes'):
				if( input('Is your cat healthy? (yes/no)\n')=='yes'):
					print('Decision: Eat it.')
				else: #is your cat healthy
					print("Decision: Your call.")
			else: #did the cat lick it
				print('Decision: Eat it.')

