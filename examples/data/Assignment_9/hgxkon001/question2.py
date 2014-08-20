#Konrad Hugo
#Assignment 9 question2

old_file = input('Enter the input filename:\n') #The inputs supplied by the user
new_file = input('Enter the output filename:\n')

text = []
line_length = 0

width = int(input('Enter the line width:\n'))
content = ''



f = open(old_file,"r") #Opens file and saves each line as list item in list_lines
list_lines = f.readlines()
f.close()

for lines in list_lines:
	if lines != '\n': 
		lines = lines.replace('\n','') #removes the \n in the occurence of consecutive non-empty lines
	else: 
		lines += '\n' #adds an extra line of space
	text += lines.split(" ") #formulates list of words without spaces

content = text[0]
line_length = len(text[0])

i=1

while i <(len(text)):
	
	if text[i] == '\n\n': 
		line_length = 0
		content += text[i]
		i += 1
		
		if i == len(text):
			break
		line_length = len(text[i])
		content += text[i]
		i += 1
	
	if i == len(text):
		break

	if (line_length + len(text[i]+' '))<=width: #This is responsible for restricting the line length, ensuring its less than or equal to the user chosen width
		content += ' '+text[i]
		line_length += len(text[i]+' ')
	else:
		content += '\n' + text[i] #This inserts a \n causing a new line to be formed when the above condition aint met
		line_length = len(text[i])
	i += 1
f = open(new_file,"w")
print(content, file=f)
	