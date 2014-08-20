# A program to determine whether or not you should eat the food
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011

# Print the welcome message
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")

def main():
	# Ask a series of questions to help the user come to a decision
	print("Answer the following questions by selecting from among the options.")
	q1 = input("Did anyone see you? (yes/no)\n")
	if q1 == "yes":
		y1 = input("Was it a boss/lover/parent? (yes/no)\n")
		if y1 == "yes":
			y2 = input("Was it expensive? (yes/no)\n")
			if y2 == "yes":
				y3 = input("Can you cut off the part that touched the floor? (yes/no)\n")
				if y3 == "yes":
					print("Decision: Eat it.")
				else:
					print("Decision: Your call.")
			else:
				n2 = input("Is it chocolate? (yes/no)\n")
				if n2 == "yes":
					print("Decision: Eat it.")
				else:
					print("Decision: Don't eat it.")
		else:
			print("Decision: Eat it.")
	else:
		sticky = input("Was it sticky? (yes/no)\n")
		if sticky == "no":
			n1 = input("Is it an Emausaurus? (yes/no)\n")
			if n1 == "yes":
				ema = input("Are you a Megalosaurus? (yes/no)\n")
				if ema == "yes":
					print("Decision: Eat it.")
				else:
					print("Decision: Don't eat it.")
			else:
				cat = input("Did the cat lick it? (yes/no)\n")
				if cat == "yes":
					healthy = input("Is your cat healthy? (yes/no)\n")
					if healthy == "yes":
						print("Decision: Eat it.")
					else:
						print("Decision: Your call.")
				else:
					print("Decision: Eat it.")
		else:
			steak = input("Is it a raw steak? (yes/no)\n")
			if steak == "yes":
				puma = input("Are you a puma? (yes/no)\n")
				if puma == "yes":
					print("Decision: Eat it.")
				else:
					print("Decision: Don't eat it.")
			else:
				cat = input("Did the cat lick it? (yes/no)\n")
				if cat == "yes":
					healthy = input("Is your cat healthy? (yes/no)\n")
					if healthy == "yes":
						print("Decision: Eat it.")
					else:
						print("Decision: Your call.")
				else:
					print("Decision: Eat it.")

main()