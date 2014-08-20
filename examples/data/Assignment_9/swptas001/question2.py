### Tashiv Sewpersad (SWPTAS001)
### CSC1015F - Assignment 9 - Q2
### 11 / 05 /2014

## Live Code
try:
	# Input Handeling
	sInFile = input("Enter the input filename:\n")
	fInFile = open(sInFile,"r")
	sOutFile = input("Enter the output filename:\n")
	iMaxWidth = eval(input("Enter the line width:\n"))
	aWords = fInFile.readlines() # creates an array of the words
	fInFile.close()

	# Create a new list containing words and newlines("\n")
	WordList = []
	for i in aWords:
		WordList.extend(i.split(" ")) # Uses single spaces as seperators 
	
	# The following removes the natural "\n" at the end of each line of text
	for i in range(1,len(WordList)):
		if (WordList[i-1] != "\n") and (WordList[i-1].find("\n") > -1):
			WordList[i-1] = WordList[i-1][:-1] # Removes "\n"
	
	# Output
	fOutFile = open(sOutFile,"w")
	iCurrentWidth = 0 # tracks line widths
	for word in WordList:
		iLen = len(word)
		# Case for paragraph split defined by user
		if word == "\n":
			print(word,file=fOutFile)
			iCurrentWidth = 0 # it starts a new line
		# First word in line case
		elif iCurrentWidth == 0:
			print(word,end="",file=fOutFile)
			iCurrentWidth = iLen
		# Second to n words case
		elif (iCurrentWidth > 0) and (iLen + iCurrentWidth + 1 <= iMaxWidth): # +1 is for the space
			print(" " + word,end='',file=fOutFile)
			iCurrentWidth += iLen + 1 # +1 is for the space
		# Case where word doesn't fit in a line
		else:
			print("\n" + word,end='',file=fOutFile)
			iCurrentWidth = iLen	

except IOError: # Handles file not found error
	print("File not found")
	
finally:
	fOutFile.close() # Closes text file