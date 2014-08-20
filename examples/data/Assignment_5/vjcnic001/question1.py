message = '' 
while True:
	selection = input(("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n"))
	if selection == "E" or selection == 'e':
		message = input("Enter the message:\n") 
	if selection == "V" or selection == 'v':
		if message == '': 
			print("The message is: no message yet")
		else:
			print("The message is:",message)
	if selection == "X" or selection == 'x':
		print("Goodbye!")
		break
	if selection == "L" or selection == "l":
		print("List of files:","42.txt,","1015.txt")
	if selection == 'd' or selection == 'D':
		file = input("Enter the filename:\n")
		if file == "42.txt":
			print("The meaning of life is blah blah blah ...")
		elif file == '1015.txt':
			print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
		else:
			print("File not found") 
	
		
		