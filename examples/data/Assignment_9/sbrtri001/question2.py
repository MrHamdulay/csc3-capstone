''' Assignment 9, question 4
Reformat a text file so that all lines are at most a given length
Tristan Subroyen
13 May 2014 '''

import textwrap

# Get user input:
filename = input("Enter the input filename:\n")
outname = input("Enter the output filename:\n")
lineWidth = eval(input("Enter the line width:\n"))

# read in the file
file = open(filename,"r")
lines = file.read()
file.close()

# format the lines of text
lines2 = textwrap.fill(lines, width=lineWidth)
lines3 = lines2.replace('  ',' ')

# write the lines of text to the output file
outfile = open(outname, "w")
print(lines3,file=outfile)
outfile.close()