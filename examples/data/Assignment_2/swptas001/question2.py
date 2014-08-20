# Assignment 2 - Question 2
# Tashiv Sewpersad
# 03 - 08 - 2014

# Heading
print("Welcome to the 30 Second Rule Expert","-"*36,"Answer the following questions by selecting from among the options.", sep="\n")

#Decision Structure
sOptions = " (yes/no)\n"
sInput = input("Did anyone see you?" + sOptions)
if sInput == "yes":
	sInput = input("Was it a boss/lover/parent?" + sOptions)
	if sInput == "yes":
		sInput = input("Was it expensive?" + sOptions)
		if sInput == "yes":
			sInput = input("Can you cut off the part that touched the floor?" + sOptions)
			if sInput == "yes":
				print("Decision: Eat it.")
			else: # no
				print("Decision: Your call.")  	
		else: # no
			sInput = input("Is it chocolate?" + sOptions)
			if sInput == "yes":
				print("Decision: Eat it.")
			else: # no
				print("Decision: Don't eat it.")		    
	else: # no
		print("Decision: Eat it.")
else: # no
	sInput = input("Was it sticky?" + sOptions)
	if sInput == "yes":
		sInput = input("Is it a raw steak?" + sOptions)
		if sInput == "yes":
			sInput = input("Are you a puma?" + sOptions)
			if sInput == "yes":
				print("Decision: Eat it.")
			else: # no
				print("Decision: Don't eat it.")			
		else: # no
			sInput = input("Did the cat lick it?" + sOptions)
			if sInput == "yes":
				sInput = input("Is your cat healthy?" + sOptions)
				if sInput == "yes":
					print("Decision: Eat it.")
				else: # no
					print("Decision: Your call.")  			
			else: # no
				print("Decision: Eat it.")  		
	else: # no
		sInput = input("Is it an Emausaurus?" + sOptions)
		if sInput == "yes":
			sInput = input("Are you a Megalosaurus?" + sOptions)
			if sInput == "yes":
				print("Decision: Eat it.")
			else: # no
				print("Decision: Don't eat it.")
		else: # no
			sInput = input("Did the cat lick it?" + sOptions)
			if sInput == "yes":
				sInput = input("Is your cat healthy?" + sOptions)
				if sInput == "yes":
					print("Decision: Eat it.")
				else: # no
					print("Decision: Your call.") 
			else: # no
				print("Decision: Eat it.")									

