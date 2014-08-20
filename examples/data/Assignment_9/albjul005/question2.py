'''Program for length adjustment to a text file
Julian Albert
16-05-2014'''
#inputs 
input_file = input('Enter the input filename:\n')
output_file = input('Enter the output filename:\n')
words = []
length_of_row = 0
output = ''
length = int(input('Enter the line width:\n'))
#opening file
f = open(input_file,"r")
lines = f.readlines()
f.close()

for line in lines:
	if line != '\n':
		line = line.replace('\n','')
	else: line += '\n'
	words += line.split(" ")

output = words[0]
length_of_row = len(words[0])

i=1
while i <(len(words)):
	if words[i] == '\n\n': 
		length_of_row = 0
		output += words[i]
		i += 1
		if i == len(words):break
		length_of_row = len(words[i])
		output += words[i]
		i += 1
	if i == len(words):break

	if (length_of_row + len(words[i]+' '))<=length:
		output += ' '+words[i]
		length_of_row += len(words[i]+' ')
	else:
		output += '\n' + words[i]
		length_of_row = len(words[i])
	i += 1
f = open(output_file,"w")
print(output, file=f)
