"""thrianka naidoo
ndxthr005
11 may 2014, assigment9, question 2: reformat and reproduce output in new file"""

input_file = input("Enter the input filename:\n")   #input for user
output_file = input("Enter the output filename:\n")
line_width = int(input("Enter the line width:\n"))

import textwrap                 #import library

f = open(input_file, "r")       #opens the input file
lines = f.read()
f.close()

wrap = textwrap.wrap(lines, line_width) #wrap the text
outputfile = open(output_file,"w") #overwrite into output textfile

for line in wrap:               #prints into new line
    print(line,file = outputfile)
outputfile.close()              #close output textfile
    

