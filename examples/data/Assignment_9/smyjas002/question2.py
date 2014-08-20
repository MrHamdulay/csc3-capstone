#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 9
#question 2

def openRead(readFile):
	words = []
	#get the desired file and read its contents-
	text = open (readFile, "r")
	lines = text.readlines ()
	text.close ()
	#process the list element by element to make it easier to understand
	for i in range (len (lines)):
		#this removes the "\n" from the end of each line if is not a completely new line
		if lines[i][:1] != "\n":
			lines[i] = lines[i][:-1] + " ~" # I used a '~' as it is obscure enough not to appear regularly, theoretically any string can be used here
		#splits the data into an two column table, name and grade
		words += lines[i].split (' ')
	return words

#writes the 'text' to the given 'writeFile'
def openWrite(text, writeFile):
	f = open (writeFile, "w")
	print (text, file=f)
	f.close ()
	
#formats a string of words into a paragraph according to the desired line length
def format(words, lineLength):
	runningLength = 0
	formatted = ""
	#adds words one by one to the program
	for word in words:
		# if it is a new paragragh "\n\n" is added for space and the characters on line count is reset to zero
		if word == "\n":
			formatted += "\n\n"
			runningLength = 0
		# if "~" comes up it means a new line was asked for in the original text and can be ignored
		elif word == "~":
			pass
		else:
			#if the word will be the first word in the line then no space is added before it
			if runningLength == 0:
				runningLength += len(word)
				formatted += word
			else:
				runningLength += len(word) + 1
				#if the total length of the line with the new word is does not exceed the line length then it is added, else it is added after a new line is created
				if runningLength <= lineLength:
					formatted += " " + word
				else: 
					formatted += "\n" + word
					runningLength = len(word)
	return formatted
		
def main():
	readFile = input("Enter the input filename:\n")
	words = openRead(readFile)
	writeFile = input("Enter the output filename:\n")
	width = int(input("Enter the line width:\n"))
	formated = format(words, width)
	openWrite(formated, writeFile)

main()
"""
 Sample File (output.txt):

Your program should store a single row
of the triangle and calculate each
subsequent row by adding a value to the
values immediately above it and to its
left.  The values on each line must be
space-separated.

Sample console I/O:

Enter the input filename:
input.txt
Enter the output filename:
output.txt
Enter the line width:
40
"""
