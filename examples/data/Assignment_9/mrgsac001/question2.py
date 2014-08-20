"""Paragraphing
Sachin Murugan
14/5/2014"""

input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
line_width = eval(input("Enter the lin width:\n"))

#open the input file

f_i = open (input_file, 'r')
lines = f_i.read()
n = lines.splitlines(True)
lines = "".join(n)

f_o = open (output_file, 'w')

newpar = lines.split("\n\n")
for line in range (len(newpar)):
	newpar[line] = newpar[line].replace("\n"," ")

format_file = [] 
for breaks in newpar:
	breaks = breaks.split(" ")
	newformat = []
	count = 0
	
	for i in breaks:
		if count + int(len(i)) <= line_width:
			newformat.append(i)
			newformat.append(" ")
			count+=int(len(i) + 1)

		else:
			newformat.append("\n")
			count = 0
			newformat.append(i)
			newformat.append(" ")
			count+=int(len(i) +1)
	format_file.append(newformat)

for i in format_file:
	if i[-1] == " ":
		i[-1] = ""
	else:
		continue 

for i in format_file:
	newlines = "".join(i)
	newlines = newlines + "\n"
	print(newlines, file=f_o)


f_i.close()
f_o.close()


#format the file by given width (hint:multiple of given width with no remainder?)
#save new formatted file to specified output file
#http://stackoverflow.com/questions/21932281/recursively-create-a-new-line-break-after-nth-character-for-a-given-block-of-tex
